from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit(X)
X_pca = pca.transform(X)

X_pca[:,0]

reg.predict(X)

reg = LinearRegression()
reg.fit(X,y)

plt.scatter(X_pca,y)
plt.plot([X_pca[X_pca.argmin()][0], X_pca[X_pca.argmax()][0]],[reg.predict(X)[X_pca.argmin()],reg.predict(X)[X_pca.argmax()]])