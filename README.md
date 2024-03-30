# driverless-car

Implements a driverless car system in a 2D world where each car receives noisy sonar estimate of the distance to other cars in the grid. The driverless car navigates the grid using this system. 

Each timestep \( t \), we measure the distance \( D_t \) between our car's position \( a_t \) and another car's position \( C_t \) using a microphone, which provides a Gaussian noise-added observation. The probability density function (PDF) for \( D_t \) can be calculated with `util.pdf(mean, std, value)`, assuming a mean equal to the actual distance and a standard deviation defined by `Const.SONAR_STD`. This model is used to estimate distances while acknowledging the presence of sensory noise.
