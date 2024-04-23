# Ant interview for SRE position
The repository contains the code for the interview process for the SRE position at Ant Financial.

## Programming & Docker
1. Write a simple web application (any language) that has 3 versions:

    a. Version 1 – display sample text (e.g. “Hello World”)

	b. Version 2 – display OS information (e.g. CPU usage)

	c. Version 3 – log access to the site to a data storage (e.g. PostgreSQL)

2. Package the web application and data storage as Docker image. Ensure each version’s image is tagged appropriately.

3. Ensure the image follows the security best practices.

## Container Orchestration
1. Create a Kubernetes cluster with 3 worker nodes.

2. Deploy the sample web application into the new cluster.

3. Demo the 3 versions of the web application.

	a. Demonstrate how an application version upgrade can be rollout and rollbacked without causing any downtime.

4. Implement metrics and logs monitoring and alerting for the web application.

## CI/CD

 1. Implement CI/CD to package and deploy the application to the cluster

## Bonus

- How to scale up (more traffic, more teams, more services) while being fast, reliable, secure. Deep dive on any of the above areas to demonstrate expertise.