function rmax=fresiduos(n,AO,x)
	for i=1:n
		soma=0;
		for j=1:n
			soma=soma+AO(i,j)*x(j);
		end %for j
		r(i)=abs(soma-AO(i,n+1));
	end %for i
  rmax=max(r);
end %function