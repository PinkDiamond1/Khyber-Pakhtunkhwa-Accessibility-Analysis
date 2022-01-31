import numpy as np
import pandas as pd
import os, sys

def rank_by_weight(df,cols_to_test,weights):
    """
    Calculate ranks based on weights applied to a series of columns to test.
    This routine is too inefficient for application to large arrays but is useful for single operations.

    Parameters
    ----------
    df : Pandas DataFrame
        A DataFrame containing the entities to test, in the order desired, and columns with the values to weight and rank by.
    cols_to_test : list (of strings)
        A list of name strings corresponding to the columns containing the values to weight, combine, and rank by
    weights: list of integers
        A list of integers of len(cols_to_test) representing the weight to apply to each col within the master index value,
        in the order the cols are specified in cols_to_test.

    Returns
    -------
    wt_rank : one Pandas Series of len(df) representing the rank for each corresponding entity under the provided weighting schema

    """

    val = np.nansum(df[cols_to_test] * weights, axis=1)

    wt_rank = pd.Series(val).rank(ascending=False).values.astype(int)

    return wt_rank

def create_weight_array(var_count=3,iterations=10000):
        """
        Create an array of arrays containing sample weights which add up to 1 (for 100%).
        Specify the numbrer of variables to divide the weights amongst and the number of samples to generate

        Parameters
        ----------
        var_count : int
            The number of variables being jointly tested.
        iterations : int
            The number of weighting schemas to generate.

        Returns
        -------
        wt_sample_array : one ndarray of shape (iterations,var_count)

        """

    #         # dirichlet distribution experiment
    #         wt = np.random.dirichlet(np.ones(var_count)*10,size=1) # * 10 moves the distribution closer to having equal weights (closer to 1./3)

        # normal distribution
        wt = np.abs(np.random.normal(np.ones((iterations,var_count)))) # size = 1 set of values, var_count columns
        wt_sample_array = (wt / np.reshape(np.sum(wt,axis=1),(iterations,1))) # normalize to 1

        return wt_sample_array

def Sensitivity_weighting(df,cols_to_test,iterations):
    """
    Use the array of weighting schemas to calculate the weighted value of each tested column, combine the results into a master index value, and calculate each entity's ranking compared to others, with larger values ranking higher.
    Implement these transformations for each row in the input weighting schema

    Parameters
    ----------
    df : Pandas DataFrame
        A DataFrame containing the entities to test, in the order desired, and columns with the values to weight and rank by.
    cols_to_test : list (of strings)
        A list of name strings corresponding to the columns containing the values to weight, combine, and rank by
    iterations : int
        The number of weighting schemas to generate and hence iterations of the sensitivity test to implement.

    Returns
    -------
    wt_sample_array : one ndarray of shape (iterations,var_count) representing the weights to use for each iteration
    vals_array : one ndarry of shape (iterations,var_count) representing the master index value per iteration
    ranks_array : one ndarry of shape (iterations,var_count) representing the rankings per iteration

    """

    var_count = len(cols_to_test)

    # create an array of noramlly distributed different weighting schemas to loop over

    wt_sample_array = create_weight_array(var_count,iterations)

    # Calculate the weighted value of each column being tested, according to each different weighting schema.
    # Store these weighted values in an equivalently sized array of values

    vals_array = np.array(df[cols_to_test]) * wt_sample_array[:,None]

    # Now calculate the entity's priority rank according to each weighting scheme
    # compute ranks array

    ranks_array = np.stack([pd.Series(np.nansum(arr,axis=1))\
                             .rank(ascending=False)
                             .values.astype(int)\
                             for arr in vals_array])

    # Ranks array process explanation:
        # calculate the sum of each row of each array
        # find the rank of each row based on its sum, make that into a series
        # pull the values out of the series back into an array (easier, trust me) and make them int
        # populate each rank array in a list of arrays
        # stack the list of arrays into one values array

    return wt_sample_array, vals_array, ranks_array

def Sensitivity_inbudget(budget,costs,ranks_array):
        """
        Create an array of arrays containing sample weights which add up to 1 (for 100%).
        Specify the numbrer of variables to divide the weights amongst and the number of samples to generate

        Parameters
        ----------
        budget : int
            The maximum budget limit for the project.
        costs : 1D ndarray
            The construction cost associated with each entity.
        ranks_array : one ndarray of shape (iterations,var_count)
            The ranking of each entity under each iteration of the weighting schemas

        Returns
        -------
        within_budget_arr : one ndarray of shape (iterations,var_count)
        within_budget_pct : one ndarray of shape (len(entities),)

        """

        # Calculate the cumulative sum along each row to understand how the budget gets taken up as entities are built along the rankings
        cumsum_arr = np.cumsum(np.concatenate(cost_arr[(ranks_array[:,None]-1)]),axis=1)

        # Revert to the original order, so the cumulative sum pertains to the correct entity (road)
        # Thanks to this SE for clarifying numpy indexing (https://stackoverflow.com/questions/37878946/indexing-one-array-by-another-in-numpy)

        cumsum_arr_ordered = cumsum_arr[np.indices(ranks_array.shape)[0],(ranks_array-1)]

        ## Create a new binary array showing whether an entity is below (1) or above (0) budget for each ranking
        within_budget_array = np.where(cumsum_arr_ordered > budget,0,1)

        # Calculate the percent of weighting schemas wherein each road is within the budget max, according to its ranking
        # Returns a 1D array of the length of the input dataframe, with values showing the % of rankings where an entity is within budget
        within_budget_pct = (np.sum(within_budget_array,axis=0) / within_budget_array.shape[0])

        return within_budget_array, within_budget_pct
