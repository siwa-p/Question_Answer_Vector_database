# Start from the existing image
FROM mcr.microsoft.com/devcontainers/base:dev-ubuntu-22.04

# Install required tools
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download Anaconda installer script
RUN curl -O https://repo.anaconda.com/archive/Anaconda3-2023.07-2-Linux-x86_64.sh

# Install Anaconda
RUN bash Anaconda3-2023.07-2-Linux-x86_64.sh -b -p /opt/anaconda && \
    rm Anaconda3-2023.07-2-Linux-x86_64.sh

# Add Anaconda to PATH
ENV PATH="/opt/anaconda/bin:$PATH"


RUN sudo apt-get update
# Activate the base Anaconda environment
SHELL ["/bin/bash", "-c"]
RUN echo "source activate base" > ~/.bashrc


# Install ML libraries
RUN conda install -y numpy pandas scikit-learn jupyter matplotlib

# Install additional packages from conda-forge
RUN conda install nltk

RUN pip install chromadb && \
    pip install ipywidgets


RUN conda install -y -c conda-forge nltk gensim scipy && \
    conda install -y -c huggingface -c conda-forge datasets huggingface_hub


RUN pip install transformers==4.36.0 && pip install -U sentence-transformers && \
    jupyter nbextension enable --py widgetsnbextension

    # had to run this again in the terminal 
    
# Set up a working directory
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]