function m = fMultiplicidade(r)
    Rlim=0.00001;
    m=1;
    somarestos=abs(r(1))+abs(r(2));
    while somarestos<Rlim
        m=m+1;
        somarestos=somarestos+abs(r(m+1));
    end
end
