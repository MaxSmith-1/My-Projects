clc, clearvars;
%Plot the Earth
eX = [];
eY = [];
for i = 0:360
    x= 6378*cosd(i);
    y= 6378*sind(i);
    eX(i+1) = x;
    eY(i+1) = y;

end
plot(eX, eY, 'b*');

hold on;


%Initialize Variables for x0, y0

x0 =  6378 + 1000;
y0 =  0;


lCell = {};
lCell{1} = "Earth";
lCount = 2;
%Gravatational Parameter
mu = 3.986*10^5;

%Change in time
dt = 10;


%Cell that will hold the list of trajectories
trajectories = cell(1,5);
trajCount = 1;

for deltaV = -2:2


%Initialize variables for each deltaV
    x = x0;
    y = y0;
    r = sqrt(x^2 + y^2);
   

    Vcirc = sqrt(mu/r);
    V0 = Vcirc + deltaV;
    Vx = 0;
    Vy = V0;

    xPos = [];
    yPos = [];
    
    count = 1;

    t=0;

    while t<10e4


        r = sqrt(x^2 + y^2);
        
        %Change Vx and Vy
        
        Vx = Vx + (((-mu)*(x)) / r^3) * dt;
        Vy = Vy + (((-mu)*(y)) / r^3) * dt;
        
        %Change X and Y, store them in a list, plot them
        
        x = x + (Vx)*dt;
        y = y + (Vy)*dt;
        


        xPos(count) = x;
        yPos(count) = y;

        count = count +1;

        t = t+dt;

        if(r<=6378)
            break;
        end
            



    end

    trajectories{trajCount} = [xPos; yPos];
    trajCount = trajCount +1;


lCell{lCount} = sprintf("Delta V = " + num2str(deltaV) + " km/s");


lCount = lCount +1;
    

end

%Plot the X and Y values
for i = 1:5
    plot(trajectories{i}(1,:), trajectories{i}(2,:));
end

legend(lCell, 'Location', 'Best');
grid on;


xlabel('x, km');

ylabel('y, km');

axis equal;


