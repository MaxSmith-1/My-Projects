clc, clearvars;

%Points initialized
t = [ 0 1 2 3 4 5 ];
h = [ 23.0 22.4 20.9 16.9 11.8 4.8 ];


%Axis Labels set
xlabel("Time, s");
ylabel("Height, cm");

%Linear and Quadratic lines of best fit found
PartB = polyfit(t,h, 1);
PartD = polyfit(t,h, 2);

%Values of these beset fit lines at t intervals found
PartBValues = polyval(PartB, t);
PartDValues = polyval(PartD, t);

%Three graphs plotted
plot(t,h, '*');
hold on;
plot(t,PartBValues);
hold on
plot(t, PartDValues);

legend("Height vs. Time", "Line of best fit (linear): " + PartB(1) + " x + " + PartB(2), "Line of best fit (quadratic): " + PartD(1) + "x^2 + " + PartD(2) + "x + " + PartD(3));


%Summing up the difference between the line of best fit values and the
%actual values squared and storing them into RMSSum variables
RMSSumPartC = 0;
RMSSumPartE = 0;
for i = 1:6
    
    RMSSumPartC = RMSSumPartC + (PartBValues(i) - h(i))^2;
    RMSSumPartE = RMSSumPartE + (PartDValues(i) - h(i))^2;
end

%Calculating the RMS for parts C and E
RMSPartC = sqrt((1/6 * RMSSumPartC))
RMSPartE = sqrt((1/6 * RMSSumPartE))