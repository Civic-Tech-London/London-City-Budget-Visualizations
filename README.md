# London City Budget Visualizations

https://drive.google.com/file/d/11mwgkpFSpDYLpQK8p0Oj-qspqgtDOBHc/preview

This project provides interactive visualizations of London's city budget, allowing users to explore and understand the allocation of funds across various departments and services.

## Installation and Usage

### Option 1: Using Docker (Recommended)

1. Clone the repository:
   ```
   git clone https://github.com/Civic-Tech-London/London-City-Budget-Visualizations.git
   ```
2. Navigate to the project directory:
   ```
   cd London-City-Budget-Visualizations
   ```
3. Use the `run.sh` script to set up the project:
   ```
   ./run.sh setup
   ```
4. Start the project:
   ```
   ./run.sh start
   ```

The `run.sh` script provides several commands to manage the Docker environment:

- `./run.sh start`: Start the project
- `./run.sh stop`: Stop the project
- `./run.sh build`: Build the Docker image
- `./run.sh setup`: Set up the project
- `./run.sh test`: Run tests
- `./run.sh shell`: Open a shell in the Docker container
- `./run.sh python`: Run Python in the Docker container
- `./run.sh pip`: Run pip commands in the Docker container

### Option 2: Local Installation

#### Requirements

- Node.js 20
- Python 3.11

1. Clone the repository:
   ```
   git clone https://github.com/Civic-Tech-London/London-City-Budget-Visualizations.git
   ```
2. Navigate to the project directory:
   ```
   cd London-City-Budget-Visualizations
   ```
3. Install dependencies:
   ```
   npm install
   ```
4. Start the development server:
   ```
   npm start
   ```

## Accessing the Application

Once the project is running, you can access it at: http://localhost:3000
