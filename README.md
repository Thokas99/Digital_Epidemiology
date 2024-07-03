# Digital Epidemiology Project: Modeling RSV Transmission in Valencia, Spain

## Table of Contents

1. [Overview](#overview)
2. [Authors](#authors)
3. [Objectives](#objectives)
4. [Methodology](#methodology)
    1. [Stochastic and Deterministic Simulations](#stochastic-and-deterministic-simulations)
5. [Repository Structure](#repository-structure)
    1. [Scripts](#scripts)
    2. [Results](#results)
6. [References](#references)

## Overview

This repository contains code and resources related to a digital epidemiology project focused on modeling the transmission of respiratory syncytial virus (RSV) in the region of Valencia, Spain. This is based on the article:

[Stochastic modeling of the transmission of respiratory syncytial virus (RSV) in the region of Valencia, Spain](https://www.sciencedirect.com/science/article/pii/S0303264709000203?casa_token=Pi9KdN2YkoQAAAAA:jB6MoDOZAnZNUfSoHWAzwBoF-XUl3OAGnPCNjJ-x2cIdxCE750DwghZy5-OcctGZ0jaxo7iIiA)

`Arenas, A. J., González-Parra, G., & Moraño, J. A. (2009). Stochastic modeling of the transmission of respiratory syncytial virus (RSV) in the region of Valencia, Spain. Biosystems, 96(3), 206-212.`

## Authors

- [Thomas Sirchi](https://github.com/Thokas99)

## Objectives

The primary objectives of this project are:

1. To reproduce the stochastic and deterministic simulations of the SIRS (Susceptible-Infectious-Recovered-Susceptible) model as described in the aforementioned paper.
2. To implement network simulation techniques to study the spread of RSV.

## Methodology

### Stochastic and Deterministic Simulations

We have replicated the stochastic and deterministic simulations of the SIRS model described by Arenas et al. in their study. Our simulations aim to understand the dynamics of RSV transmission and the impact of different parameters on disease spread.

### Network Simulation

Additionally, we have conducted network simulations to model the spread of RSV. By representing individuals as nodes and their interactions as edges in a network, we aim to capture the complex patterns of disease transmission.

## Repository Structure
### [scripts](scripts)
This directory includes the primary scripts for simulations and analysis, such as:
- [`Final_Euler_Maruyama_method_BIRTH`](scripts/Final_Euler_Maruyama_method_BIRTH.ipynb): Script for stochastic SIRS model simulation with birth perturbation.
- [`Final_Euler_Maruyama_method_TRASMISSION`](scripts/Final_Euler_Maruyama_method_TRASMISSION.ipynb): Script for stochastic SIRS model simulation trasmission perturbation.
- [`Final_method_SOLVE_IVP`](scripts/Final_method_SOLVE_IVP.ipynb): Script for deterministic, RK45, SIRS model simulation.

### [results](results)
This directory stores the results of simulations and analyses, including:
- Plots and graphs generated from the simulations.
- Summary statistics and output files from the models.

## References

- Arenas, A. J., González-Parra, G., & Moraño, J. A. (2009). Stochastic modeling of the transmission of respiratory syncytial virus (RSV) in the region of Valencia, Spain. Biosystems, 96(3), 206-212.
