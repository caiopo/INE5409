function c = fcoefMaclaurin(n)
    c(1) = log(5.5);

    for i = 1 : n
        c(i+1)=(-1)^(i+1)*((10-1)/(10+1))^i/(i);
    end
end
