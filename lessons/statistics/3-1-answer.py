resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh,label='actual')
pmf_biased = BiasPmf(pmf,label='observed')
thinkplot.preplot(2)
thinkplot.Pmfs([pmf, pmf_biased])
thinkplot.Config(xlabel='number of children per household', ylabel='PMF')

actual_mean = pmf.Mean()
biased_mean = pmf_biased.Mean()
