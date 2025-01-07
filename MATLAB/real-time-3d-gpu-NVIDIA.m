% 3D Sierpiński-tetraéder GPU-val
clc;
clear;

% Tetraéder csúcsai
A = [0, 0, 0];
B = [1, 0, 0];
C = [0.5, sqrt(3)/2, 0];
D = [0.5, sqrt(3)/6, sqrt(2/3)];

% Iterációk száma
iterations = 10000;

% Kezdőpont véletlenszerűen
current_point = gpuArray([0.5, 0.5, 0.5]);  % A pontok GPU-ra kerülnek

% Ábra beállítása
figure;
hold on;
axis equal;
xlim([0, 1]);
ylim([0, 1]);
zlim([0, 1]);
title('Sierpiński-tetraéder (GPU)');
xlabel('X');
ylabel('Y');
zlabel('Z');

% Frissítési frekvencia
refresh_rate = 100;

% Iterációk
for i = 1:iterations
    % Véletlenszerűen kiválasztunk egy csúcsot
    random_vertex = randi(4);
    if random_vertex == 1
        target = gpuArray(A);
    elseif random_vertex == 2
        target = gpuArray(B);
    elseif random_vertex == 3
        target = gpuArray(C);
    else
        target = gpuArray(D);
    end
    
    % Új pont számítása (felezőpont)
    current_point = (current_point + target) / 2;
    
    % Pont kirajzolása
    plot3(current_point(1), current_point(2), current_point(3), 'b.', 'MarkerSize', 1);
    
    % Progresszió és ábra frissítése
    if mod(i, refresh_rate) == 0
        percent_complete = (i / iterations) * 100;
        fprintf('Progress: %.2f%%\n', percent_complete);
        drawnow;
    end
end

% Végső állapot
fprintf('Progress: 100.00%% - Done!\n');
