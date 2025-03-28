# Multi-Cloud Terraform Infrastructure

## Project Description

This Terraform project demonstrates infrastructure management using Docker as a provider. It creates multiple containerized web application instances on a single network.

### Features

- Dynamic container creation
- Configurable container count
- Custom Docker network
- Flexible image selection

### Prerequisites

- Terraform (version 0.14+)
- Docker
- Docker provider for Terraform

### Initialize Terraform

```
terraform init

```

### Preview Infrastructure Changes

```
terraform plan

```

### Apply Configuration

```
terraform apply

```

### Destroy Infrastructure

```
terraform destroy

```

### Initialize Terraform

```
terraform init

```


### Outputs

- container_ids: IDs of created containers
- container_names: Names of created containers
- network_name: Name of the Docker network

### Customization

Modify variables.tf to change default container settings:

- Adjust container_count for more/fewer instances
- Change container_image to use different Docker images

