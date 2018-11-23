function c = fcoefMaclaurin(n)
    for i = 0 : n
        sgn = (-1) ** floor(i/2);
        c(i+1) = sgn * (pi**i) / (2 ** (2*i + 0.5) * factorial(i));
    end
end
