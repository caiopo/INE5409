function [ A B ] = ftrocalinhasLUCrout (k,A,B)
n = size(A,1);  %Numero de linhas de A

% Vmax é maior valor da coluna k, buscando nas linhas de k até n
Vmax=abs(A(k,k));
linhaMax=k;
for i=k+1:n
  if abs(A(i,k))>Vmax
     Vmax=abs(A(i,k));
     linhaMax=i;
  end
end

%Trocas de linhas, em A e B:
aux=A(k,:);
A(k,:)=A(linhaMax,:);
A(linhaMax,:)=aux;

aux=B(k,:);
B(k,:)=B(linhaMax,:);
B(linhaMax,:)=aux;

end
