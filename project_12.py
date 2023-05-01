#Creating an empty list
services = []

#Adding services to the list
services.append("cloud9")
services.append("EC2")
services.append("S3")
services.append("Lambda")
services.insert(0, "VPC")

#printing the list and length of the list
print(services)
print(len(services))

#removing two items from the list
del services[1]
del services[1]

#printing the list and length of the list again
print(services)
print(len(services))
