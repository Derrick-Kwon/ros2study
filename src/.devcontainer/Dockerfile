FROM ros:humble

ARG USERNAME=hjkwon
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Update & basic dev tools
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    python3-pip \
    build-essential \
    git \
    curl \
    wget \
    lsb-release \
    gnupg2 \
    locales \
    python3-colcon-common-extensions \
    ros-humble-desktop \
    ros-humble-rqt* \
    ros-humble-rviz2 \
    ros-humble-tf2-tools \
    ros-humble-image-tools \
    libopencv-dev \
    && apt-get clean

# Set locale (optional)
RUN locale-gen en_US en_US.UTF-8 && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
ENV LANG en_US.UTF-8

ENV SHELL /bin/bash

# Default to non-root user
USER $USERNAME
CMD ["/bin/bash"]
