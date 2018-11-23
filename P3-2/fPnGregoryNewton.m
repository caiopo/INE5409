function yp = fPnGregoryNewton(n, tp)
    [a, t] = fCoefPnGregoryNewton(n, [-1, 1]);

    for r = 1 : length(tp)
        yp(r) = a(1);
        for k = 1 : n
            aux = 1;
            for j = 1: k
                aux = aux * ((tp(r) - t(j)));
            end
            yp(r) = yp(r) + a(k+1) * aux;
        end
    end
end
