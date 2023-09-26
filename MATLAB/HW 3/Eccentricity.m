clc, clearvars;

Rp = 1.5;

%Hyperbola theta max


%Plot Earth 

eX = [];
eY = [];
for i = 0:360
    x=cosd(i);
    y=sind(i);
    eX(i+1) = x;
    eY(i+1) = y;

end
plot(eX, eY, 'bo');

hold on;

%Loop through eccentricities


lCell = {};
lCell{1} = "Earth";
lCount = 2;


for e = 0:.25:2

    


    %Loop through unit circle to get x,y coordinates
    xList = [];
    yList = [];

if e<=1
    for d = 0:360

        
        r = (Rp*(1+e)) / (1 + (e)*(cosd(d)));
        
        x = (r)*(cosd(d));

        y = (r)*(sind(d));

      
        xList(d+1) = x;

        yList(d+1) = y;
       

        
            



    end


else


    thetaMin = -1* round(-1*.9*acosd(-1/e));
    thetaMax = round(-1*.9*acosd(-1/e));
    count = 1;
    for d = thetaMax:thetaMin

        r = (Rp*(1+e)) / (1 + (e)*(cosd(d)));
        
        x = (r)*(cosd(d));

        y = (r)*(sind(d));

      
        
        xList(count) = x;

        yList(count) = y;

        count = count +1;
       




end


end








plot(xList, yList)



lCell{lCount} = sprintf("e = " + num2str(e));


lCount = lCount +1;





hold on


end


legend(lCell, 'Location', 'Best');
grid on;
axis equal;

xlabel('x, Earth radii');

ylabel('y, Earth radii');

axis([-12 12 -10 10])




