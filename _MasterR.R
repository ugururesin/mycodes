########################################
# FUNDAMENTAL AND ADVANCED CODES in R
# Prepared by Ugur Uresin, Data Engineer
################################################################################
# A- BASICS
# B- DATA OPERATIONS
# C- PLOTTING
# D- STATISTICS
# E- MACHINE LEARNING
# F- DATA ENGINEERING (APPLY FUNCTIONS INCLUDED)
################################################################################

# NOTE: USE THIS FORMAT IF IT FITS
########################################
# DEFINITON:  Small explanation
# FORMAT:     A generic R code
# ATTENTION:  Critical points (if there are)
#
# EXAMPLE     (if needed)
########################################

#R-Python Integration
########################################
install.packages("reticulate")
library("reticulate")

#GOING IN PYTHON PLATFORM
repl_python()
a=2
b=5
c="NAME"
exit

#Assigning the vars to R
r_a = py$a
r_b = py$b
r_c = py$c
########################################

################################################################################
# A- BASIC CODES 
################################################################################
# A1-DIRECTORY SETTING
# A2-HELLO WORLD!
# A3-PACKAGE INSTALL & USE
# A4-DATA IMPORT/REMOVE & DIRECTORY SET
# A5-SPECIAL CHARACTERS
# A6-INDEXES
# A7-LOGICAL OPERATIONS
# A8-ARITHMETIC OPERATIONS
################################################################################

# 1-DIRECTORY SETTING
########################################
# MAC:
setwd("/Users/ugur/Desktop/R/")
# Windows:
setwd("C:\\Users\\ugur\\Desktop\\R")
# Reaching a subfolder in current wdir
setwd("./Subfolder_name")   # MAC
setwd(".\\Subfolder_name")  # Windows


# 2-HELLO WORLD!
########################################
for(i in 1:5){print("Hello World")}


# 3-PACKAGE INSTALL & USE
########################################
install.packages("package.name")
library(package.name)


# 4-DATA IMPORT/REMOVE & DIRECTORY SET
########################################
# Data Import From Internet
data01 <- read.csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", sep=",",header=F) #sep for seperator, header=T if there are headers
# Data Import From Local (MAC)
data02 = read.csv("/Users/UGUR/Desktop/R/_data/titanic_data/test.csv")
# Data Import with RowNames
data02 <- read.csc("mydata", row.names=1) #1st column goes to the rownames!
# Open a Window to Selecet the Data to be Imported 
my_data <- read.delim(file.choose())  #For .txt tab file
my_data <- read.csv(file.choose())    #For .csv file
# Removing All Content Except for X
rm(list=setdiff(ls(), "X"))


# 5-SPECIAL CHARACTERS
########################################
# ~   Alt+n or Alt+ü
# ≈   Alt+x
# ®   Alt+r
# ∫   Alt+b
# √   Alt+v
# ≤   Alt+ö
# ≥   Alt+ç


# 6-INDEXES
########################################
# R starts from 1, JAVA starts from 0
A <- c(6,4,3,1,0)
A[1] #R Gives:6, JAVA Gives:4


# 7-LOGICAL OPERATIONS
########################################
# OR Operator
5==4 | 5<=6   #For "|" sign: Alt+-
# AND Operator
5==4 & 5<=6


# 8-ARITHMETIC OPERATIONS
########################################
# Round Function
round(5.2) #goes 5
round(5.7) #goes 6
round(5.5) #goes 6
round(5.566, digits=2) #goes 5.57


################################################################################
# B- DATA OPERATION CODES in R
################################################################################
# B1-NA & NULL
# B2-GENERIC DATA FUNCTIONS
# B3-VECTORS
# B4-MATRICES
# B5-ARRAYS
# B6-DATA FRAMES
# B7-LISTS
# B8-FACTORS
# B9-DATA CONVERSIONS
################################################################################


# B1-NA & NULL
########################################
# DEFINITION: Both NA & NULL represent a 'Missing' or 'Not Entered' value
# DIFFERENCE: NULL has a class but NA!


# B2-GENERIC DATA FUNCTIONS
########################################
object <- c("Tim"=1,"Sue"=2,"Tom"=3)
object
length(object)  #Number of elements or components
str(object)     #Structure of an object 
class(object)   #Class or type of an object
names(object)   #Names
#
c(object,object)      #Combine objects into a vector
cbind(object,object)  #Combine objects as columns
rbind(object,object)  #Combine objects as rows
#
ls()       #List current objects
rm(object) #Delete an object
#
newobject <- edit(object) #Edit copy and save as newobject 
fix(object)               #Edit in place
# DATA RANGES
mydata1 <- c(1,2,5,9)
mydata2 <- c(3,4,6,7)
range(mydata1,mydata2)
range(0,mydata1,mydata2) #Starts from 0
########################################


# B3-VECTORS
########################################
# Note: For arithmetic operations, the sizes must be same!!!
#
# VECTOR TYPES
my_vector <- c(1,2,3,4,5)    #vector type is double
my_vector <- c("mr","mrs")   #vector type is character
my_vector <- c(T,F)          #vector type is logical
my_vector <- c(1,T,"mr")     #vector type is character
my_vector <- 1:5; x          #creates a vector in a given range!
my_vector <- seq(1,2,by=0.2)        #creates a vector with a step size!
my_vector <- seq(1,5,length.out=3)  #creates a vector with an interval and size!
# ACCESS TO ELEMENTS
my_vector[1]                #1st element of the myvector
my_vector[c(1,2)]           #1st and 2nd elements of the myvector
my_vector[my_vector<0]      #negative elements of the myvector
my_vector[my_vector>0]      #positive elements of the myvector
# ASSIGN INDEX
my_vector <- c("first"=3,"second"=5,"third"=7)
my_vector
# COMBINE NUMERIC VECTORS
a <- c(1,2,3,4)
b <- c(5,6,7,8)
coldata <- cbind(a,b) # merge two vector as two cols
rowdata <- rbind(a,b) # merge two vector as two rows


# B4-MATRICES
########################################
# NOTE: All columns in a matrix must have the same mode(numeric, character, etc.) 
#
# MATRIX CREATION
mymatrix <- matrix(1:9, nrow=3, byrow=T) # byrow=T/F is to order elements byrow
# COL AND ROW NAMES
colnames(mymatrix) <- c("A","B","C")
rownames(mymatrix) <- c("D","E","F")
mymatrix
# COMBINE MATRICES
A <- matrix(c(1,2,3,4),ncol=2,byrow=F)
B <- matrix(c(5,6))
C <- matrix(c(8,9))
cbind(A,B)
rbind(B,C)


# B5-ARRAYS
########################################
# Arrays are similar to matrices but can have more than two dimensions


# B6-DATA FRAMES
########################################
# NOTE: A data frame is more general than a matrix
# Different columns can have different modes (numeric, character, factor, etc.)
#
# DF CREATION (WAY 1)
d <- c(1,2,3,4)
e <- c("red", "blue", "grey", NA)
f <- c(TRUE,TRUE,TRUE,FALSE)
mydf1 <- data.frame(d,e,f)
names(mydf1) <- c("ID","Color","Passed") #variable names
mydf1
# DF CREATION (WAY 2)
mydf2 <- data.frame(
  Names=c("Tom","Sue","Kim","Joe"),
  Gender=c("M","F","F","M"))
mydf2


# B7-LISTS
########################################
# DEFINITION: An ordered collection of objects (components)
# A list allows you to gather a variety of (possibly unrelated) objects under one name
#
# LIST CREATION
mylist <- list("mycharacter", myvector, mylogical)
#
# ACCESSING AN ELEMENT IN A LIST
mylist[[1]][3]		#gives the 3rd element in the 1st col
mylist$name[3]		#gives the 3rd element in the "name" col 
#
# ACCESSING SOME COMPONENTS IN A LIST
mylist[c(1:4)]		#gives the first 4 cols
mylist[c(1,5)]		#gives the 1st and 5th cols
#
# NAMING COMPONENTS OF A LIST
names(mylist) <- c("Name1","Name2","Name3") 		#1st Way (For a existing list)
mylist <- list(Name1=col1, Name2=col2, Name3=col3)	#2nd Way (When creating a list)
#
# EXTRACTING COMPONENTS OF A LIST
# 3 Ways
# []    will always return a list
# [[]]  will always return the actual list
# $     same as [[]] but prettier
#
# REARRANGING COLUMNS IN A DF
mydata <- NULL
mydata <- mydata[,c(4,1,2,3)] 	#arrange cols by 4th,1st,2nd,3rd
#
# REMOVE A COL (Example 4th col)
mylist[4] <- NULL 				#ATTENTION: NUMERATION SHIFTS AFTER REMOVE!!!
#
# FINDING COL1 VALUES THAT HAS NA IN A COL3
mylist[is.na(mylist$COL3NAME),"COL1NAME"]



# B8-FACTORS
########################################
# Factors are basically character variables (Example: Female and Male)
# Names should NOT be categorized as factors (Example: Ali, Tom, Sue)
#
# FACTOR CREATION
answers=c("T","T","F","E","T","T","E")          #Gives 7 characters
summary(answers)                        
answersF=factor(answers,levels=c("T","F","E"))  #Gives 3 factors w different frequencies
summary(answersF)
#
# FACTOR LEVEL SETTING:
X=c("Fair","Good","Very Good","Premimum","Ideal")
is.ordered(X)         #Gives FALSE!
orderedX=factor(X,levels=c("Fair","Good","Very Good","Premimum","Ideal"),ordered=T)
is.ordered(orderedX)  #Gives TRUE!
#
# FACTOR VARIABLE TRAP (FVT)
########################################
# DEFINITON:  Transforming a factor containing numbers to numerical value
#             gives the position of the levels (instead of content of the variable)!
#
# EXAMPLE 
a <- c("12","13","14","12","12")          #Converting chars into numerics
typeof(a)							                    #character
b <- as.numeric(a)					              
typeof(b)							                    #double (No Problem Here)
#
z <- factor(c("12","13","14","12","12"))  #Converting factors into numerics
z									                        #factor w levels: 12 13 14
typeof(z)							                    #integer
y <- as.numeric(z)	
y                                         #gives "1 2 3 1 1" (it means 1st factor, 2nd factor, 3rd factor, 1st factor, 1st factor): FVT Problem!!!
# CORRECT WAY:  Convert into char then into num
x <- as.numeric(as.character(z))


# B9-DATA CONVERSIONS
########################################
# KEEPING ORIGINAL FORMAT IN DATA FRAMES
x=1:10
y=c("a","b","c","d","e","f","g","h","i","j")
z=c(T,F,T,T,F,T,T,T,T,T)
mymatrix=cbind(x,y,z)
mydataframe=data.frame(x,y,z)     #Variable types are preserved
str(mydataframe)
mydataframe2=data.frame(mymatrix) #Variable types are NOT preserved. Because MATRIX turns all into FACTORS!
str(mydataframe2)
#
# WRONG ORDERING IN NUMERICS!
# EXAMPLE
mydataframe2$w = as.numeric (mydataframe2$x)    #This is WRONG!!!
mydataframe2$w                                  #New col (w) is ordered as 1,3,4,5... instead of 1,2,3,4...
str(mydataframe2)
# CORRECT WAY1: First convert vectors into char, add to data.frame then convert into num
# CORRECT WAY2: At the beginning; use vectors to create dataframe, NOT matrices!
mydataframe$w = as.numeric(mydataframe$x)
str(mydataframe)


################################################################################
# C- PLOTTING CODES
################################################################################
# C1-SAVING A PLOT
# C2-SCATTER PLOTS
# C3-BAR CHARTS
# C4-HISTOGRAMS
# C5-PIE CHARTS
# C6-DOT CHARTS
# C7-MISC
# C8-GGPLOT (Special Plot Package)
# C9-TIME SERIE CREATION (GGPLOT)
################################################################################


# C1-SAVING A PLOT
########################################
mydata1 <- c(1,2,3,5,8)                             #Example data to plot
plot(mydata1, type="o", col="blue", pch=1, lty=1)   #Plots mydata1
setwd("/Users/ugur/Desktop/R/")                     #Set a directory to save the plot
dev.copy(png,'myplotname.png')
dev.off()


# C2-SCATTER PLOTS
########################################
# MAIN TYPES
mydata1 <- c(1,2,3,5,8)
plot(mydata1, type="p", col="blue")  #"p" for points,
plot(mydata1, type="l", col="blue")  #"l" for lines,
plot(mydata1, type="b", col="blue")  #"b" for both,
plot(mydata1, type="c", col="blue")  #"c" for the lines part alone of "b",
plot(mydata1, type="o", col="blue")  #"o" for both ‘overplotted’,
plot(mydata1, type="h", col="blue")  #"h" for ‘histogram’ like (or ‘high-density’) vertical lines,
plot(mydata1, type="s", col="blue")  #"s" for stair steps,
plot(mydata1, type="S", col="blue")  #"S" for other steps, see ‘Details’ below,
plot(mydata1, type="n", col="blue")  #"n" for no plotting
# DATA POINT TYPE: pch parameter
plot(mydata1, type="o", col="blue", pch=1)  #1 for circle
plot(mydata1, type="o", col="blue", pch=2)  #2 for triangle
plot(mydata1, type="o", col="blue", pch=3)  #3 for +
plot(mydata1, type="o", col="blue", pch=4)  #4 for x 
plot(mydata1, type="o", col="blue", pch=8)  #8 for *
plot(mydata1, type="o", col="blue", pch=22) #22 for square
# DATA LINE TYPE: lty parameter
plot(mydata1, type="o", col="blue", pch=1, lty=1)  #1 for continuous
plot(mydata1, type="o", col="blue", pch=1, lty=2)  #2 for line-dashed
plot(mydata1, type="o", col="blue", pch=1, lty=3)  #3 for point-dashed
plot(mydata1, type="o", col="blue", pch=1, lty=4)  #4 for line-point-dashed
plot(mydata1, type="o", col="blue", pch=1, lty=5)  #5 for line-dashed (longer)
plot(mydata1, type="o", col="blue", pch=1, lty=6)  #6 line-point-dashed (longer)
# EDITING AXES
plot(mydata1, type="o", col="blue", ylim=c(0,10))   #Defines limits of y-axis
plot(mydata1, type="o", col="blue", xlim=c(0,10))   #Defines limits of y-axis
plot(mydata1, type="o", col="blue", ann=F)          #Plots wo Titles
title(xlab="My X Axis Title", col.lab="red")        #Defines X-Axis Title
title(ylab="My Y Axis Title", col.lab="red")        #Defines Y-Axis Title
title(main="MyTitle", col.main="red", font.main=1)  #Adds Title (1:Normal, 2:Bold, 3:Italic, 4:BoldItalic ...)
# RE-DEFINING AXES
mydata2 <- c(2,4,6,3,7)
myrange <- range(mydata2)
plot(mydata2, type="o", col="blue", axes=F, ann=F)    #Creates a Plot wo Axes & Titles 
axis(1, at=1:5, lab=c("Mon","Tue","Wed","Thu","Fri")) #Creates a below axis (1=below, 2=left, 3=above and 4=right)
axis(2, las=1, at=0:myrange[2])                       #Creates a left axis with the 'Data Range' (las=3 to rotate the label)
box()                                                 #Creates a box around the plot
# MULTIPLE PLOTTING & LEGEND
mydata1 <- c(1,2,3,5,8)
mydata2 <- c(2,4,6,3,7)
myrange <- range(mydata1,mydata2)
plot(mydata1, type="o", col="blue", pch=1, lty=1)   #Plots mydata1
lines(mydata2, type="o", col="red", pch=4, lty=2)   #Adds mydata2 into previous plot
legend(1,myrange[2], c("data1","data2"), col=c("blue","red"), pch=c(1,4), lty=c(1,2))  #1,myrange[2] is the (x,y) position of the legend, instead can be "topleft"
# PLOTS FOR LM
house=data.frame(
  size=c(80,90,105,120,130,140,150,170,205),
  price=c(135,145,165,195,205,215,225,250,285)
)

plot(x=house$size, y=house$price, xlab="Size m2", ylab="Price k$")  #To plot house data
abline(lm(formula= price~., data=house),col="red")                  #To draw the prediction curve (lm) 


# C3-BAR CHARTS
########################################
mybardata <- c(1,3,6,4,9)
barplot(mybardata)
# EXAMPLE
autos_data <- data.frame(
  cars=c(1,3,6,4,9),
  trucks=c(2,5,4,5,12),
  suvs=c(4,4,6,6,16)
)
# Hatched Bar Charts
barplot(autos_data$cars, main="Cars", xlab="Days", ylab="Total",
        names.arg=c("Mon","Tue","Wed","Thu","Fri"), border="blue", density=c(10,20,30,40,50)) #density parameter is to hatch on bars
# Adjacent bars using rainbow colors
barplot(as.matrix(autos_data), main="Autos", ylab= "Total", beside=TRUE, col=rainbow(5))      #rainbow(5) is for 5 different colors
# Place the legend at the top-left corner with no frame using rainbow colors
legend("topleft", c("Mon","Tue","Wed","Thu","Fri"), cex=0.8, bty="n", fill=rainbow(5));
# Expand right side of clipping rect to make room for the legend
par(xpd=T, mar=par()$mar+c(0,0,0,4))
# Graph autos (transposing the matrix) using heat colors,put 10% of the space between each bar, and make labels smaller with horizontal y-axis labels
barplot(t(autos_data), main="Autos", ylab="Total", 
        col=heat.colors(3), space=0.1, cex.axis=0.8, las=1,
        names.arg=c("Mon","Tue","Wed","Thu","Fri"), cex=0.8) 
# Place the legend at (6,30) using heat colors
legend(6, 30, names(autos_data), cex=0.8, fill=heat.colors(3));
# Restore default clipping rect
par(mar=c(5, 4, 4, 2) + 0.1)


# C4-HISTOGRAMS
########################################
# BASIC HISTOGRAM
autos <- data.frame(
  cars=c(1,3,6,4,9),
  trucks=c(2,5,4,5,12),
  suvs=c(4,4,6,6,16)
)
hist(autos$cars)
hist(autos$cars, col="blue")
# MULTIPLE HISTOGRAM
autos_data <- c(autos$cars, autos$trucks, autos$suvs) #concatenate the three vectors
max_num <- max(autos_data)
hist(autos_data, col=heat.colors(max_num), xlim=c(0,max_num), breaks=max_num, right=F, main="Autos Histogram", las=1) #las for axis number alignment
# PROBABILITY DENSITY
autos_data <- c(autos$cars, autos$trucks, autos$suvs) #concatenate the three vectors
max_num <- max(autos_data)
brk <- c(0,3,4,5,6,10,16)
# Create a histogram for autos with fire colors, set uneven breaks,
# make x axis range from 0-max_num, disable right-closing of cell intervals,
# set heading, make y-axis labels horizontal, make axis labels smaller,
# make areas of each column proportional to the count
hist(autos_data, col=heat.colors(length(brk)), breaks=brk, xlim=c(0,max_num), right=F, main="Probability Density", las=1, cex.axis=0.8, freq=F)
#
# DISTRIBUTION HISTOGRAMS
# Get a random log-normal distribution
r <- rlnorm(1000)
hist(r)
# Get a random log-normal distribution
r <- rlnorm(1000)
h <- hist(r, plot=F, breaks=c(seq(0,max(r)+1, .1))) # Get the distribution without plotting it using tighter breaks
# Plot the distribution using log scale on both axes, and use blue points
plot(h$counts, log="xy", pch=20, col="blue", main="Log-normal distribution", xlab="Value", ylab="Frequency")


# C5-PIE CHARTS
########################################
# EXAMPLE
cars <- c(1, 3, 6, 4, 9)
pie(cars)
# Create a pie chart with defined heading and custom colors and labels
cars <- c(1, 3, 6, 4, 9)
pie(cars, main="Cars", col=rainbow(length(cars)), labels=c("Mon","Tue","Wed","Thu","Fri"))
# Change the colors, label using percentages, and create a legend
colors <- c("white","grey70","grey90","grey50","black")                   #Defines some colors ideal for black & white print
car_labels <- round(cars/sum(cars) * 100, 1)                              #Calculates the percentage for each day, rounded to one decimal place
car_labels <- paste(car_labels, "%", sep="")                              #Concatenates a '%' char after each value
pie(cars, main="Cars", col=colors, labels=car_labels, cex=0.8)            #Creates a pie chart with defined heading and custom colors and labels
legend(1.5, 0.5, c("Mon","Tue","Wed","Thu","Fri"), cex=0.8, fill=colors)  #Creates a legend at the right   


# 6-DOT CHARTS
########################################
# EXAMPLE
autos <- data.frame(
  cars=c(1,3,6,4,9),
  trucks=c(2,5,4,5,12),
  suvs=c(4,4,6,6,16)
)
dotchart(t(autos))
# Create a colored dotchart for autos with smaller labels
dotchart(t(autos), color=c("red","blue","darkgreen"), main="Dotchart for Autos", cex=0.8)


# C7-MISC
########################################
# This example shows all 25 symbols that you can use to produce points in your graphs:
# Make an empty chart
plot(1, 1, xlim=c(1,5.5), ylim=c(0,7), type="n", ann=FALSE)
# Plot digits 0-4 with increasing size and color
text(1:5, rep(6,5), labels=c(0:4), cex=1:5, col=1:5)
# Plot symbols 0-4 with increasing size and color
points(1:5, rep(5,5), cex=1:5, col=1:5, pch=0:4)
text((1:5)+0.4, rep(5,5), cex=0.6, (0:4))
# Plot symbols 5-9 with labels
points(1:5, rep(4,5), cex=2, pch=(5:9))
text((1:5)+0.4, rep(4,5), cex=0.6, (5:9))
# Plot symbols 10-14 with labels
points(1:5, rep(3,5), cex=2, pch=(10:14))
text((1:5)+0.4, rep(3,5), cex=0.6, (10:14))
# Plot symbols 15-19 with labels
points(1:5, rep(2,5), cex=2, pch=(15:19))
text((1:5)+0.4, rep(2,5), cex=0.6, (15:19))
# Plot symbols 20-25 with labels
points((1:6)*0.8+0.2, rep(1,6), cex=2, pch=(20:25))
text((1:6)*0.8+0.5, rep(1,6), cex=0.6, (20:25))


# C8-GGPLOT (Special Plot Package)
########################################
# PACKAGE INSTALL:
install.packages("ggplot2")
library(ggplot2)
#
# STRUCTURE:
vectorx <- c(1,2,3,4)
vectory <- c(2,4,6,8)
mydata <- cbind(vectorx,vectory)
ggplot(data=mydata)                                 #Takes the data
+geom_function(mapping = aes(x=vectorx, y=vectory)) #Assigna the vectors to the axes
#
# EXAMPLE:
house=data.frame(
  size=c(80,90,105,120,130,140,150,170,205),
  price=c(135,145,165,195,205,215,225,250,285)
)
ggplot(data=house)+
  geom_point(mapping=aes(x=size,y=price))+
  coord_cartesian(ylim=c(100,300))+
  geom_smooth(mapping=aes(x=size, y=price),method="lm",formula=y~x,se=T)  #The grey area is the 'confidence interval' (se=F to close)
#
# SCATTER PLOT:
library(ggplot2)
View(ggplot2::mpg)  #Data in ggplot2 package
mpgdata <- mpg
plot(mpgdata$displ,mpgdata$hwy)
plot(x=mpgdata$displ,y=mpgdata$hwy,col="red", xlab="Volume", ylab="Mile/Gallon",
     main="Engine Volume vs. Fuel Consumption",
     sub="Based on mpg data in ggplot2", type="p")
ggplot(data=mpgdata) + geom_point(mapping = aes(x=displ, y=hwy))
#
# MULTIPLE PLOT:
g1 <- ggplot(data=mpgdata) + geom_point(mapping = aes(x=displ, y=hwy))
g2 <- ggplot(data=mpgdata) + geom_point(mapping = aes(x=displ, y=cty))
easyGgplot2::ggplot2.multiplot(g1,g2)
#
# DISPLAY & EMPHASIZE LABELS (class)
mpgdata$class = as.factor(mpgdata$class)  # First, convert 'class' into a factor then add to geom_point (col, size, shape...)
# Seperating by Color
g11=ggplot(data=mpgdata)+geom_point(mapping=aes(x=displ, y=hwy, col=class))+ggtitle("Consumption in Highway")
g22=ggplot(data=mpgdata)+geom_point(mapping=aes(x=displ, y=hwy, col=class))+ggtitle("Consumption in City")
g11
g22
easyGgplot2::ggplot2.multiplot(g11,g22)   #ATTENTION: This may collapse R. Expand plots window as large as possible!
# Separating by Point Size
ggplot(data=mpgdata)+geom_point(mapping=aes(x=displ, y=hwy, size=class))
# Separating by Point GreyScale (Alpha Parameter)
ggplot(data=mpgdata)+geom_point(mapping=aes(x=displ, y=hwy, alpha=class))
# Separating by Point Shape (Shape Parameter)
ggplot(data=mpgdata)+geom_point(mapping=aes(x=displ, y=hwy, shape=class))  #ATTENTION: shape can display 6 parameters in max!
# Separating by Point Shape and Color Together
ggplot(data=mpgdata)+geom_point(mapping=aes(x=displ, y=hwy, shape=class, col=class))+ggtitle("Consumption in Highway")
# Album Plots (facet_wrap) function
ggplot(data=mpgdata)+geom_point(mapping=aes(x=displ, y=hwy))+facet_wrap(~class,nrow=2)
#
# BAR-CHARTS:
elmas=ggplot2::diamonds
# Note: in geom_bar, y is count as default, only x is required to be defined
ggplot(data=elmas)+geom_bar(mapping=aes(x=cut,color=cut))                                 #bars w colored edges
ggplot(data=elmas)+geom_bar(mapping=aes(x=cut,fill=cut))                                  #bars w filled colors
ggplot(data=elmas)+geom_bar(mapping=aes(x=cut,fill=cut))+theme(legend.position = "none")  #removes the legend
# To Show 2nd Categoric Variable in Bars
ggplot(data=elmas)+geom_bar(mapping=aes(x=cut,color=clarity))
ggplot(data=elmas)+geom_bar(mapping=aes(x=cut,fill=clarity))
# Position parameter
ggplot(data=elmas)+geom_bar(mapping=aes(x=cut,fill=clarity),position="stack") #gives count
ggplot(data=elmas)+geom_bar(mapping=aes(x=cut,fill=clarity),position="fill")  #gives %count
# Identity parameter
elmas=diamonds[1:3,]
ggplot(data=elmas)+geom_bar(mapping=aes(x=cut,y=carat),stat="identity")


# C9-TIME SERIE CREATION (GGPLOT)
########################################
p <- ggplot(data=mydata)
p + geom_line(aes(x=Mytime, y=Myresult,colour=Myfactors), size=1.2) +
  facet_grid(Myfactors~.) +
  geom_hline(yintercept = 1.0, colour="Gray", size=1.2, linetype=3) #adds a threshold line on y=1


################################################################################
# D- STATISTICAL OPERATIONS
################################################################################
# D1-INITIAL DATA CHECK
# D2-CENTAL TENDENCY AND VARIABILITY
# D3-RELATIVE STANDING
# D4-t TESTS
# D5-ANOVA
# D6-CORRELATION & REGRESSION
################################################################################


# D1-INITIAL DATA CHECK
########################################
head(mydata)    #shows first 6 rows of the data
tail(mydata)	  #shows last 6 rows of the data
tail(mydata,8)	#shows last 8 rows of the data
summary(mydata)	#shows the statistics of the data


# D2-CENTAL TENDENCY AND VARIABILITY
########################################
x <- c(10,20,30)
mean(x)   #Mean of the numbers in vector x.
median(x) #Median of the numbers in vector x
var(x)    #Estimated variance of the population from which the numbers in vector x are sampled
sd(x)     #Estimated standard deviation of the population from which the numbers in vector x are sampled
scale(x)  #Standard scores (z-scores) for the numbers in vector x
str(x)    #Displays the internal structure


# D3-RELATIVE STANDING
########################################
x <- c(30,10,20)
n <- 1
sort(x)     #The numbers in vector x in increasing order
sort(x)[n]	#The nth smallest number in vector x
rank(x)     #Ranks of the numbers (in increasing order) in vector x
rank(-x)    #Ranks of the numbers (in decreasing order) in vector x
quantile(x)	#The 0th, 25th, 50th, 75th, and 100th percentiles (i.e, the quartiles) of the numbers in vector x
rank(x,ties.method="average") #Ranks of the numbers (in increasing order) in vector x, with tied numbers given the average of the ranks that the ties would have attained
rank(x,ties.method="min")     #Ranks of the numbers (in increasing order) in vector x, with tied numbers given the minimum of the ranks that the ties would have attained
rank(x,ties.method="max")     #Ranks of the numbers (in increasing order) in vector x, with tied numbers given the maximum of the ranks that the ties would have attained


# D4-t TESTS
########################################
x <- c(1,2,3,4)
y <- c(5,6,7,8)
n <- 2.5

t.test(x,mu=n, alternative="two.sided") #Two-tailed t-test that the mean of the numbers in vector x is different from n.
t.test(x,mu=n, alternative="greater")	  #One-tailed t-test that the mean of the numbers in vector x is greater than n.
t.test(x,mu=n, alternative="less")	    #One-tailed t-test that the mean of the numbers in vector x is less than n.
t.test(x,y,mu=0, var.equal=TRUE, alternative="two.sided") #Two-tailed t-test that the mean of the numbers in vector x is different from the mean of the numbers in vector y. The variances in the two vectors are assumed to be equal.
t.test(x,y,mu=0, alternative="two.sided", paired=TRUE)    #Two-tailed t-test that the mean of the numbers in vector x is different from the mean of the numbers in vector y. The vectors represent matched samples.

# D5-ANOVA
########################################
x <- c(1,2,3,4)
y <- c(5,6,7,8)
z <- c(2,4,6,8)
w <- c(2,3,4,5)
d <- as.data.frame(cbind(x,y))
aov(y~x, data = d)                #Single-factor ANOVA, with the numbers in vector y as the dependent variable and the elements of vector x as the levels of the independent variable. The data are in data frame d.
aov(y~x + Error(w/x), data = d)   #Repeated Measures ANOVA, with the numbers in vector y as the dependent variable and the elements in vector x as the levels of an independent variable. Error(w/x) indicates that each element in vector w experiences all the levels of x (i.e., x is a repeated measure). The data are in data frame d.
aov(y~x*z, data = d)              #Two-factor ANOVA, with the numbers in vector y as the dependent variable and the elements of vectors x and z as the levels of the two independent variables. The data are in data frame d.
aov(y~x*z + Error(w/z), data = d) #Mixed ANOVA, with the numbers in vector z as the dependent variable and the elements of vectors x and y as the levels of the two independent variables. Error(w/z) indicates that each element in vector w experiences all the levels of z (i.e., z is a repeated measure). The data are in data frame d.


# D6-CORRELATION & REGRESSION
########################################
x <- c(1,2,3,4)
y <- c(2,4,6,9)
z <- c(1,1,1,2)
d1 <- as.data.frame(cbind(x,y))
d2 <- as.data.frame(cbind(x,y,z))
cor(x,y)          #Correlation coefficient between the numbers in vector x and the numbers in vector y
cor.test(x,y)     #Correlation coefficient between the numbers in vector x and the numbers in vector y, along with a t-test of the significance of the correlation coefficient.
# Linear Regression
mymodel <- lm(y~x, data = d1) #Linear Regresion Model
coefficients(mymodel)         #Slope and intercept of linear regression of mymodel
confint(mymodel)              #Confidence intervals of the slope and intercept of linear regression of mymodel
lm(y~x+z, data = d2)          #Multiple regression analysis with the numbers in vector y as the dependent variable and the numbers in vectors x and z as the independent variables. Data are in data frame d.
lm(y~., data = d2)            #"." can be written for all variables except from y in the d2 data


################################################################################
# E- MACHINE LEARNING CODES
################################################################################
# E1-SIMPLE LINEAR REGRESSION 
# E2-DECISION TREES
# E3-Simple kNN
# E4-CONVOLUTIONAL NEURAL NETWORK
# E5-RANDOM-FOREST
# E6-NAIVE BAYES
########################################


# E1-SIMPLE LINEAR REGRESSION (Simple Means 1 Variable)
########################################
# EXAMPLE (Let's Predict the Price of a House According to its Size)
house=data.frame(
  size=c(80,90,105,120,130,140,150,170,205),
  price=c(135,145,165,195,205,215,225,250,285)
)
# MODEL CREATION
y_price=lm(formula=price~size,data=house)   # price~. takes all variables (except price) as independent variables
# STATISTICS OF THE MODEL
summary(y_price)
# "Estimate":     When the variable (size) increases by 1 unit, how much price increases?
# "Multiple R2":  Only with the variable (size) how much can we explain the price?      
# "P-value":      if it's <0.05, the variable (size) is statistically significant
#
# PREDICTION MAKING
example.sizes=data.frame(
  size = c(75,100,125,180)
)
price_predictions = predict(y_price,example.sizes)  #prediction parameter is set
price_predictions                                   #prediction result is given

plot(x=house$size, y=house$price)                   #To plot house data
abline(lm(formula= price~., data=house),col="red")  #To draw the prediction curve (lm) 


# E2-DECISION TREES
########################################
# DEFINITION: Do not predict numeric but factors!
# ATTENTION:  Not a good predictor but has a good visualization!
#
# PACKAGE INSTALL:
install.packages("tree")
library(tree)
# EXAMPLE:
car <- read.csv("/Users/UGUR/Desktop/R/_data/car_data/car.data",sep=",",header=F)     #ASK the data uresinugur35@gmail.com
heads <- c("Price","MaintenanceCost","Doors","Seats","Luggage","Safety","Evaluation") #DO NOT USE SPACE in HEADER NAMES!!!
names(car) <- heads
View(car)
car <- as.data.frame(car)
# TREE FUNCTION
?tree
# MODEL CREATION
my.decision.tree = tree(Evaluation~., data=car)
#RESULTS
my.decision.tree
#PLOTTING
plot(my.decision.tree)
text(my.decision.tree)          #Default, text size is not the optimal
plot(my.decision.tree)
text(my.decision.tree, cex=0.75) #cex=text size
#PREDICTION MAKING
new.car=car[140,]
newcar.result = predict(my.decision.tree, new.car)
newcar.result   #the result would be "unacc"


# E3-Simple kNN ALGORITHM
########################################
# EXAMPLE
a=c(160,163,168,175,180,190,165,170,185,184,191,168,178,163,176)  #heights of a sample
b=c(50,52,70,59,80,85,51,63,79,70,72,57,60,70,90)                 #weights of a sample
s=c("F","F","M","F","M","M","F","M","M","F","F","M","F","M","M")  #genders of a sample
gender=as.factor(s)
(mydata = data.frame(Height=a,Weight=b,Gender=s))
# PLOTTING
install.packages("ggplot2")
library(ggplot2)
ggplot(mydata)+geom_point(aes(x=Height,y=Weight,col=Gender))
#
# PREDICTION MAKING
library("class")                    #Default package in R, no need to install
# Prediction Example1
person1=c(180,65)
result1 = knn(cbind(a,b),person1,s) #default k=1
result1
# Prediction Example2
person2=c(187,75)
results2 = knn(cbind(a,b),k=3,person2,s)  #try different k values
results2
#
# TRAIN & TEST kNN
# EXAMPLE
install.packages("ISLR")
library("ISLR")
??Caravan                  #Read the description of the data
View(Caravan)             #Look the data 
dim(Caravan)              #Dimension of the data is 5822*86
karavan=Caravan           #Assign the data so that the original is kept
summary(karavan$Purchase) #5474 NO, 348 YES
karavan2=karavan[,-86]    #Extracting the non-numeric value
# NORMALIZING
karavan2=scale(karavan2)
View(karavan2)
sqrt(var(Caravan[,2]))
mean(var(Caravan[,2]))
# MODEL CREATION
test =1:1000
test.X=karavan2[test,]            #Use first 1000 X value for testing
train.X=karavan2[-test,]          #Use left X values for training
#
test.Y=karavan$Purchase[test]     #Use first 1000 Y value for testing
train.Y=karavan$Purchase[-test]   #Use left Y values for training
#
prediction_model = knn(train.X, test.X, train.Y, k=5)
mean(test.Y !=prediction_model)
mean(test.Y !="No")
mean(test.Y !="Yes")
#
# PREDICTION MAKING
table(prediction_model,test.Y)
#


# E4-CONVOLUTIONAL NEURAL NETWORK
########################################
# NOTE: All Variables Must Be Numeric for CNN!!!
#
# EXAMPLE:
# PACKAGE INSTALL FOR DATA: Boston
install.packages(MASS)
library(MASS)
# PACKAGE INSTALL FOR: neuralnet 
install.packages("neuralnet")
library(neuralnet)
#
# DATA CHECK
View(Boston)
# The variable to be predicted must be between 0 and 1
# Other variables must be subtracted from their means and divided to their standard deviations.
# NORMALIZING THE VARIABLE TO BE PREDICTED (medv)
Boston.scaled <- as.data.frame(scale(Boston))
min.medv <- min(Boston$medv)
max.medv <- max(Boston$medv)
Boston.scaled$medv <- scale(Boston$medv, center = min.medv, scale = max.medv - min.medv)
# TRAIN & TEST DATA PARTITION
Boston.train.scaled <- Boston.scaled[1:400, ]
Boston.test.scaled <- Boston.scaled[401:506, ]
# MODEL CREATION
# All variables must be written one by one when using the NN function!
# Use the model.matrix function if you have a variable with multiple categories (?model.matrix)
# First Model (2 hidden layers with 5&3 nodes)
Boston.nn.5.3 <- neuralnet(medv~crim+zn+indus+chas+nox+rm+age+dis+rad+tax+ptratio+black+lstat,
                           data=Boston.train.scaled,
                           hidden=c(5,3),
                           linear.output=TRUE)
plot(Boston.nn.5.3)         #To display the neural-network
#Second Model (1 hidden layer with 8 nodes)
Boston.nn.8 <- neuralnet(medv~crim+zn+indus+chas+nox+rm+age+dis+rad+tax+ptratio+black+lstat,
                         data=Boston.train.scaled,
                         hidden=8,
                         linear.output=TRUE)
plot(Boston.nn.8)           #To display the neural-network


# E5-RANDOM-FOREST ALGORITHM
########################################
# EXPLANATION: Uses multiple trees
#
# PACKAGE INSTALL
install.packages("randomForest")
library("randomForest")
#
# INFO
# ntree:  Number of tress to grow
# ntry:   Number of variables randomly sampled as candidates at each split
#
# EXAMPLE DATA
?Titanic
View(Titanic)
str(Titanic)
# DATA CONVERSION
myTitanic           <- as.data.frame(Titanic) #To keep original data 
myTitanic$Survived  <- as.factor(myTitanic$Survived)
myTitanic$Sex       <- as.factor(myTitanic$Sex)
myTitanic$Age       <- as.factor(myTitanic$Age) #not given as num but Adult/Child
myTitanic$Freq      <- as.numeric(myTitanic$Freq)
str(myTitanic)
#
# MODEL CREATION
rf = randomForest(Survived ~ Class + Sex + Age + Freq, data=myTitanic, ntry=2, ntree=1000)
#There are 7 variables, ntry should be sqrt(5)≈2
#
# CONFUSION MATRIX
rf$confusion
#
# PREDICTION
titanic.set1 <- data.frame(Class=c("1st","1st","2nd","2nd","3rd","3rd","Crew"),
                           Sex=as.factor(c("Male","Female","Female","Male","Male","Female","Male")),
                           Age=as.factor(c("Adult","Child","Adult","Adult","Adult","Child","Adult")),
                           Freq=c(1,1,1,1,0,0,0),
                           Survived=as.factor(c("No","Yes","Yes","No","No","Yes","No"))
                           )
str(titanic.set1)
View(titanic.set1)
(mypredictions = predict(rf, titanic.set1))
(comparison <- table(mypredictions, titanic.set1$Survived))
(accuracy <- (comparison[1]+comparison[4])/sum(comparison))


################################################################################
# F- DATA ENGINEERING
################################################################################
# F1-GSUB() and SUB()
# F2-DATA-FILTERS for Missing & Non-Missing Data
# F3-REPLACING MISISNG DATA: FACTUAL ANALYSIS METHOD
# F4-REPLACING MISISNG DATA: MEDIAN IMPUTATION METHODS (3 METHODS)
# F5-APPLY FUNCTIONS
################################################################################


# F1-GSUB() and SUB()
########################################
# DEFINITON:  To replace instances
# FORMAT:     mydata$colA <- gsub("kph","mph",mydata$colA)    it replaces kph with mph in colA in mydata
# ATTENTION:  gsub() converts the instances to chr!
#             gsub() replaces all while sub() replaces only the first match
# EXAMPLE
mydata <- list(Industry=as.factor(c("Auto Industry","Auto Industry","Auto Industry","Auto Industry","Information Technologies Industry","Information Technologies Industry","Information Technologies Industry","Information Technologies Industry")),
               Employees=as.integer(c(3000,1000,750,500,2500,1500,500,300)),
               Region=as.factor(c("US","EU","EU","ME","US","US","EU","ME")),
               Revenue=as.factor(c("$12,5M","$9,5M","$7M","$3M","$23M","$17M","$6,5M","$2M"))
)
head(mydata)
#
# To replace "Information Technologies" with "IT 
mydata$Industry <- gsub("Information Technologies","IT",mydata$Industry)
head(mydata)
#
# To replace " Industry" with nothing!
mydata$Industry <- gsub(" Industry","",mydata$Industry)
head(mydata)
#
# To replace "$" with nothing! (NOTE: $ is a special sign, must be written as \\$)
mydata$Revenue <- gsub("\\$","",mydata$Revenue)
head(mydata)
#
# DATATYPE CORRECTION
# gsub convert the instances to chr. Now convert them to num!
mydata$Industry <- as.factor(mydata$Industry)
mydata$Revenue <- as.factor(mydata$Revenue)
str(mydata)


# F2-DATA-FILTERS for Missing & Non-Missing Data
########################################
# DEFINITON:  To Locate Non-Missing/Missing Data
# FORMAT:     complete.cases(mydata) or !complete.cases(mydata)
#
# EXAMPLE
setwd("/Users/ugur/Desktop/R/_data/r_advanced/")
fin <- read.csv("future_500.csv",na.strings=c("")) #to replace empty chars with NA
fin[!complete.cases(fin),]
#
# which() for non-missing data
# DEFINITION: which indices are TRUE
head(fin)
fin[fin$Employees==45,]         # gives the rows that Employees=45 including Employess=NA!
fin[which(fin$Employees==45),]  # gives the rows that Employees=45 not including Employess=NA!
#
# is.na() for missing data
# EXAMPLE
a <- c(1,2,3,NA,5,6,NA)
is.na(a) # F F F T F F T
# EXAMPLE2
is.na(fin$Expenses)
fin[is.na(fin$Expenses),] # gives the rows that includes NA
#
# Removing records with missing data
fin_backup <- fin
fin[!complete.cases(fin),]
fin[is.na(fin$Industry),]
fin[!is.na(fin$Industry),] #opposite
fin <- fin[!is.na(fin$Industry),]
fin
#
# Resetting the dataframe index
fin
rownames(fin) <- 1:nrow(fin)
fin
rownames(fin) <- NULL
fin


# F3-REPLACING MISISNG DATA: FACTUAL ANALYSIS METHOD
########################################
# FORMAT: mydata[is.na(mydata$country) & mydata$city=="Boston","country"] <- "USA" (city and country are the example cols)
# EXAMPLE
#
# DATA IMPORT & CHECKS
setwd("/Users/ugur/Desktop/R/_data/r_advanced/")
fin <- read.csv("future_500.csv")
fin <- read.csv("future_500.csv",na.strings=c(""))  #to replace empty chars with NA
fin[!complete.cases(fin),]                          #to get cols. that have missing values
fin[is.na(fin$State),]                              #checking 'NA's in State col.
# CASE: Filling NA states with according to the their city values!
fin$State[c(11,379,84,267)]  #check the states (All four are NA)
fin[is.na(fin$State) & fin$City=="New York",]                     #show the rows that State=NA & City=New York
fin[is.na(fin$State) & fin$City=="New York","State"] <-"NY"       #to assign "NY" to the states (State=NA & City=New York)
fin[is.na(fin$State) & fin$City=="San Francisco",]                #show the rows that State=NA & City=San Francisco
fin[is.na(fin$State) & fin$City=="San Francisco","State"] <-"CA"  #to assign "CA" to the states (State=NA & City=San Francisco)
fin$State[c(11,379,84,267)]      #check the states again
#


# F4-REPLACING MISSING DATA: 
########################################
# MEDIAN IMPUTATION METHOD-1
# EXPLANATION:  #Missing values can be filled with average/median of the relevant column
                #Taking average/median not for all rows but only related rows is logical
# EXAMPLE
#
# THE DATA
setwd("/Users/ugur/Desktop/R/_data/r_advanced/")
fin <- read.csv("future_500.csv")
fin <- read.csv("future_500.csv",na.strings=c(""))  #to replace empty chars with NA
# THE CASE
# In fin data some of the "Employees" cells are missing
# Missing values can be filled with average/median of the relevant column
# Taking average/median not for all rows but only related rows is logical
#
fin[!complete.cases(fin$Employees),]  #not-complete "Employees" values in fin data (3,332)
#
# EXAMPLE1: Filling NA cells with Median in "Retail"
med_empl_retail <- median(fin[fin$Industry=="Retail","Employees"], na.rm=T)                     #med calculation
med_empl_retail -> fin[is.na(fin$Employees) & fin$Industry=="Retail","Employees"]               #assign the med
fin[3,] #check the missing employee value becomes 28
#
# EXAMPLE2: Filling NA cells with Median in Financial Services"
med_empl_finserv <- median(fin[fin$Industry=="Financial Services","Employees"], na.rm=T)        #med calculation
med_empl_finserv #80
med_empl_finserv -> fin[is.na(fin$Employees) & fin$Industry=="Financial Services","Employees"]  #assign the med
fin[332,] #check the missing employee value becomes 80
#
# MEDIAN IMPUTATION METHOD-2
# THE CASE
# In fin data some of the "Growth" cells are missing
fin[!complete.cases(fin$Growth),]  #not-complete "Growth" values in fin data (8)
View(fin)
# Growth values are given with % sign, so we need to get rid of it
fin$Growth <- gsub("%","",fin$Growth)
View(fin)
as.numeric(fin$Growth) -> fin$Growth
#
med_growth_constr <- median(fin[fin$Industry=="Construction","Growth"], na.rm=T)    #med calculation
med_growth_constr #10
med_growth_constr ->fin[is.na(fin$Growth) & fin$Industry=="Construction","Growth"]  #assign the med
fin[8,]
#
# MEDIAN IMPUTATION METHOD-3
# THE CASE
# In fin data some of the "Expenses" cells are missing
# Data Editing
View(fin)
fin$Expenses <- gsub(" Dollars","",fin$Expenses)
fin$Expenses <- gsub(",","",fin$Expenses)
fin$Expenses <- as.numeric(fin$Expenses)
#
fin[is.na(fin$Profit),"Profit"] 
med_exp_constr
med_exp_constr -> fin[is.na(fin$Expenses) & fin$Industry=="Construction","Expenses"]
fin[c(8,44),]
#
# Deriving Values for Profit
# Profit = Revenue - Expenses
str(fin)
fin$Profit <- as.numeric(fin$Profit)
View(fin)
fin$Revenue <- gsub("\\$","",fin$Revenue)
fin$Revenue <- gsub(",","",fin$Revenue)
fin$Revenue <- as.numeric(fin$Revenue)
View(fin)
fin[is.na(fin$Profit),"Profit"] <- fin[is.na(fin$Profit),"Revenue"] - fin[is.na(fin$Profit),"Expenses"]
View(fin)
#
# Deriving Values for Expenses
# Expenses = Revenue - Profit
fin[is.na(fin$Expenses),"Expenses"] <- fin[is.na(fin$Expenses),"Revenue"] - fin[is.na(fin$Expenses),"Profit"]
fin[15,]


# F5-APPLY FUNCTIONS
########################################
# APPLY FUNCTION
# DEFINITON:  Works as a single line loops
# FORMAT:     There are numerous formats, check examples
#
# EXAMPLE (Mean Calculation)
?apply
apply(mylist, 1, mean)  #1 for rows, 2 for columns
# Alternative way (Inefficient way!!!)
output <- NULL
for(i in 1:5){
  output[i] <- mean(mylist[i,])
}
output
#
# LAPPLY FUNCTION
# DEFINITON:  Apply a FUNCTION over a List or Vector
# FORMAT:     There are numerous formats, check examples
#
# EXAMPLES
lapply(mylist, t)                   #transpose
lapply(mylist, rbind, NewRow=1:10)	#rbind (1:10 is given as example)
#
#Combining lapply with the [] operator
lapply(mylist, "[", 1,1)	#Gives first row firts col elements of all subdata
lapply(mylist, "[", 1)		#Gives first rows of all subdata
lapply(mylist, "[", 3)		#Gives 3rd cols of all subdata
#
#Adding your own functions
lapply(mylist, function(x) x[1,]) #function is applied to the 1st rows of the subdata in mylist
lapply(mylist, function(z) z[1,]-z[2,]) #function is applied to difference btw 1st and 2nd rows
#
# SAPPLY FUNCTION
# DEFINITON:  A user-friendly version and wrapper of lapply
# FORMAT:     There are numerous formats, check examples
#
# EXAMPLE DATA (SunGlasses Sales)
glasses <- list(Model1=rbind(Shop=(c("Spring"=c(31),"Summer"=c(75),"Autumn & Winter"=c(33))),
                            Online=(c("Spring"=c(69),"Summer"=c(85),"Autumn & Winter"=c(14)))),
               Model2=rbind(Shop=(c("Spring"=c(64),"Summer"=c(73),"Autumn & Winter"=c(11))),
                            Online=(c("Spring"=c(92),"Summer"=c(91),"Autumn & Winter"=c(13))))
               )
               
glasses
# Let's find online sales in spring
lapply(glasses, "[", 2, 1)     #Gives 2nd Row, 1st Col
sapply(glasses, "[", 2, 1)     #Gives 2nd Row, 1st Col in a Vector (Prettier)
# Let's find shop sales in spring and summer
lapply(glasses, "[", 2, 1:2)   #Gives 2nd Rows of '1st and 2nd Cols'
sapply(glasses, "[", 2, 1:2)   #Gives 2nd Rows of '1st and 2nd Cols' in a Matrix (Prettier)
# Let's find means for the sale platforms (Shop vs. Online)
lapply(glasses, rowMeans)      #Gives the row means
sapply(glasses, rowMeans)      #Gives the row means in a Matrix (Prettier)
#
# Round all Values
round(sapply(glasses, rowMeans), 2)
#
# Sale Diffences between Shop and Online
lapply(glasses, function(z) abs(z[1,]-z[2,])) 
sapply(glasses, function(z) abs(z[1,]-z[2,])) #Much prettier!
#
# NESTING APPLY FUNCTIONS
apply(glasses$Model1, 1, max)   #max can be applied on a table (Model1)
apply(glasses, 1, max)          #max can NOT be applied on a list (glasses)!!!
sapply(glasses, apply, 1, max)  #max of the every single row in the list
#
# TO FIND OUT "WHEN/WHICH" MAX AND MIN VALUES OCCUR  
sapply(glasses, apply, 1, max)
sapply(glasses, apply, 1, min)
# 
?which.max #check the function
#
#EXAMPLE
which.max(glasses$Model1[1,])         #gives the COL NAME and the COL NUMBER of the MAX VALUE!
names(which.max(glasses$Model1[1,]))  #gives the COL NAME of the MAX VALUE!
#
apply(glasses$Model1, 1, function(x) names(which.max(x))) #gives COL NAMEs of the max values in the rows (Model1)
apply(glasses$Model2, 1, function(x) names(which.max(x))) #gives COL NAMEs of the max values in the rows (Model2)
sapply(glasses, function(y) apply(y, 1, function(x) names(which.max(x)))) #gives COL NAMEs of the max values in the rows (All!)
#
