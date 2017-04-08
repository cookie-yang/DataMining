function [] = kmeansHW(k)

%load the dataset

[name a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15 a16]=textread('zoo.txt','%s%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d','delimiter', ',');
X=[a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15 a16];

idx = kmeans(X,k,'Display','iter');
% 'iter' means the iteration times will be automatically determined.

%[idx,C] = kmeans(X,k); 
%idx = kmeans(X,k) partition the n-by-p data matrix X into k clusters
%and returns an n-by-1 vector (idx) containing cluster indices 
%kmeans uses the squared Euclidean distance measure and the k-means++ algorithm

for i=1:k
 s=[];
 fprintf('%s%d%s','class ',(i-1),': ');
 for j=1:size(name)
  if idx(j)==i
    s=strjoin([s name(j)]);
  end
 end
 fprintf('%s\n',s);
end