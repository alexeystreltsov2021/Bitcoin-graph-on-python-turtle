  When I was watching the "Python in 6 Hours" video while learning the requests module,there was an example involving sending a request to an exchange to receive Bitcoin prices.
That's when I got the idea to visualize the exchange data as a graph. That's when the first version of this graph was created.
At first, the graph was quite primitive, but it worked. However, it had many significant flaws. For example, there was no proper zoom level—you had to manually move the screen.
Although there were stripes in the background, they weren't labeled, so you had to count from the labeled starting point.
The current price was also displayed, listed below the current chart endpoint. However, this wasn't a solution, as the text disappeared as soon as the chart advanced, which happened every second.
Another significant drawback is the short time the chart runs, since a few minutes after launching the program, the chart moves beyond the visible part of the screen and becomes invisible.
You might think that increasing the screen size along the X axis would solve all the problems, but the problem is that when scrolling forward on the chart, you have to scroll a very small distance, which is difficult and inconvenient to do manually.
I tried setting up automatic screen scrolling, but for some reason, it kept breaking everything.
	That's all that can be said about the first version of the graph, but the second version has far fewer errors. Let's start with the fact that the graph is now drawn not as a line like a cardiogram, but as on normal exchanges, with red and green candlesticks. 
In the second version of the chart, I fixed the scaling issue by making everything on a single screen of fixed dimensions.
As for the illustration of the current price, I've improved it very well. Briefly, above the graph, I've added space for tables with the current price, maximum price, current time, and so on.
Additionally, there are bars in the background that are labeled on the right side of the screen and can be easily scaled.The hardest part was coming up with a formula that would allow the graph to work correctly at any Bitcoin price.
In other words, if the scale is 0.01 (this isn't the scale of the lines; the scale of the lines is how many dollars are in the gap between two adjacent lines!), everything will be fine with a price range of around $1,000.
But if the price is around $100,000,then the graph won't work as intended because the price will be converted to a coordinate along the y-axis and will be equal to 1000 (by the way, the screen height is 700) and the graph will only just begin and will no longer be visible. 
Thanks to my formula, no matter what the price, at the beginning of the program, the scale for this specific price range is calculated using the formula,
therefore the graph always visible.
	But even though the second version is much better than the first, I'm going to make a third version that will combine the two previous ones.
