function Y=H(n,a,b,x,y1,y2,y3,y4,D)
    [x y1 y2 y3 y4]=fRK4sist4(n,a,b,x,y1,y2,y3,y4); %resolve o sistema uma vez para 
    %y3(1)=C(1) e y4(1)=C(2)
    Y(1)=y1(n+1)-D(1);
    Y(2)=y2(n+1)-D(2);
end
