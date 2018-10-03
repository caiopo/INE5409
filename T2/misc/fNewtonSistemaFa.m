% Calcular as raízes pelo método de Newton com derivada numérica
% dfi/dxj = (Fa(xi(1) + ... +  x(j) + dx(j) +...+ xi(n) + Fa(xi(1)+ ... + xi(n))))/dx(j)

function x = fNewtonSistemaFa(n, xi)
    tolerance = 1e-14;
    for i = 1 : n
        dx(i) = 2 * tolerance;
    end

    dx = transpose(dx);

    k = 0;
    while (max(abs(dx)) > tolerance) & (k < 50)
        k++;
        % Criando Matrix Jacobiana
        for j = 1 : n
            xnovo = xi;
            xnovo(j) = xi(j) + dx(j);
            A(:, j) = (Fa(xnovo) - Fa(xi))/dx(j);
        end
        A;
        B = -Fa(xi);

        dx = A \ B;
        x = xi + dx;
        xi = x;

    end
end
