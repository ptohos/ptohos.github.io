def lineFit(x,y):
    '''
    Returns slope annd y-intercept 
    of linear fit to (x,y) data set
    '''
    xavg = x.mean()
    slope = (y * (x-xavg)).sum()/(x * (x-avg)).sum()
    yint = y.mean() - slope * xavg
    return slope, yint
