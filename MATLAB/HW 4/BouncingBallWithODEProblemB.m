clc, clearvars

%Function called
[t,s, aT, aH] = bouncingBallA(2, 7, 1000, 1, 2.5);

%Plot of height vs. time
plot(t,s(:, 1), 'b*')
hold on;

%Plot of apogees
plot(aT, aH)

xlabel("Time (s)");
ylabel("Height (m)");
grid on;


%Function defined
function [times,state,apogeeTimes,apogeeHeights] = bouncingBallA( h0, tmax, k, M, D)

ge = 9.8;

% Initial conditions:
h = h0;
V = 0;

apogeeTimes = [];
apogeeHeights = [];

state0 = [ h V ]'; % Per ode45 specifications: state must be column vector

%Ode option set to find apogee points
options = odeset('Events', @isApogee);

% Integrate equations of motion -- note that drag is computed by propagator
[times, state, te, ye, ie] = ode45( @bouncingBallOde, [ 0 tmax ], state0, options);

%Apogee points given to values given by 'isApogee' function
apogeeTimes = te;
apogeeHeights = ye(:, 1);


%Function to determine apogee points
function [value, isterminal, direction, ah, at] = isApogee( t, state )


value(1) = state(2); % Notice when velocity < 0
isterminal(1) = 0;
direction(1) = -1; % Notice only when velocity is decreasing



    end

% Function giving state derivative
    function d = bouncingBallOde( t, state )

%state vector: h, V
h = state(1);
V = state(2);


d = zeros(2,1); % Column vector to hold state derivatives
d(1) = V;
d(2) = -ge;

if h < 0
    d(2) = d(2) - (((k*h) + (D*V))/M); %Alters acceleration of ball when the ball hits the ground
end

end % of inner function



end % of outer function




