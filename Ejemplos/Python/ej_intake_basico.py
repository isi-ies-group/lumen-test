import intake
cat = intake.open_catalog("catalog_intake.yaml")
# this is a simple iterator which will pass the values 1, 2, 3
# with no control. We choose to print each value as it arrives
# s0 = cat.simple.read()
# s0.sink(print)
# and now we run the iterator and see the values printed
# s0.start()
# this is a streaming dataframe
s = cat.df.read()
# at first, nothing is shown, since the stream has not been started
# s
# it supports plotting via hvplot, which stores a history by default
s.plot()
# now we actually start the stream
# the dataframe and plot both display
s.start()
# but we could have plotted directly, which starts the source automatically
# but note that this is a new stream of random numbers
cat.df.plot()
# also we defined a custom plot in the catalogue, which is just
# a new name for scatter
cat.df.plots
# this is how you access it
cat.df.plot.myscatter()
