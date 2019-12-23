---
layout: review
permalink: /:categories/:title/
category: Notes
tag: 笔记
---

## Beta distribution

In probability theory and statistics, the beta distribution is a family of continuous probability distributions defined on the interval $[0, 1]$ parametrized by two positive shape parameters, denoted by $\alpha$ and $\beta$, that appear as exponents of the random variable and control the shape of the distribution. It is a special case of the Dirichlet distribution.

PDF: $\frac{x^{\alpha-1}(1-x)^{\beta-1}}{\mathrm{B}(\alpha, \beta)}$, where $\mathrm{B}(\alpha, \beta)=\frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha+\beta)}$ and $\Gamma$ is the Gamma function.



## Dirichlet distribution

$\operatorname {Dir} ({\boldsymbol {\alpha }})$ is a family of continuous multivariate probability distributions parameterized by a vector ${\boldsymbol {\alpha }}$ of positive reals. It is a multivariate generalization of the beta distribution, hence it has an alternative name of multivariate beta distribution (MBD). Dirichlet distributions are **commonly used as prior distributions in Bayesian statistics**, and in fact the Dirichlet distribution is the conjugate prior of the categorical distribution and multinomial distribution.

PDF: $\frac{1}{\mathrm{B}(\boldsymbol{\alpha})} \prod_{i=1}^{K} x_{i}^{\alpha_{i}-1}$, where $\mathrm{B}(\boldsymbol{\alpha})=\frac{\prod_{i=1}^{K} \Gamma\left(\alpha_{i}\right)}{\Gamma\left(\sum_{i=1}^{K} \alpha_{i}\right)}$ and $\boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{K}\right)$.



## Stochastic block model

The stochastic block model is a generative model for random graphs. This model tends to produce graphs containing communities, subsets characterized by being connected with one another with particular edge densities. For example, edges may be more common within communities than between communities. The stochastic block model is important in statistics, machine learning, and network science, where it serves as a useful benchmark for the task of recovering community structure in graph data.

The stochastic block model takes the following parameters:

- the number $n$ of vertices
- a partition of the vertex set $\{1,\ldots,n\}$ into disjoint subsets ${C_{1},\ldots ,C_{r}}$, called *communities*
- a symmetric ${r\times r}$ matrix ${P}$ of edge probabilities.

The edge set is then sampled at random as follows: any two vertices $u \in C_i$ and $v \in C_j$ are connected by an edge with probability $P_{ij}$. An example problem is: given a graph with $n$ vertices, where the edges are sampled as described, recover the groups $C_1,\ldots,C_r$.

