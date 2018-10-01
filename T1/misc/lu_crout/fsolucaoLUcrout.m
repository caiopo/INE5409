function X = fsolucaoLUcrout(A,B)


    [A B] = decomp_lu_crout(A,B);

    A
    B

    for j = 1 : size(B,2)
        X(:,j) = fcalculaCx(A,B(:,j));
    end
end
