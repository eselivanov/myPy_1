def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.
           Returns string."""

    # contruct string from the dictionary of parametrs
    return "; ".join(["%s=%s" % (k, v) for k, v in params.items()])


# when module is used as a standalone program i.e. for debug:
if __name__ == "__main__":
    myParams = {"server":"mpilgrim1", \
                "database":"master1", \
                "uid":"sa1", \
                "pwd":"secret1" \
                }
    print( buildConnectionString(myParams) )
