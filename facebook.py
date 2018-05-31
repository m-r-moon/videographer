###############################
# Filename: post.py           #
# Author: Mitchel R Moon      #
###############################

import facebook

graph = facebook.GraphAPI(access_token='token', version='2.12')

graph.put_object(parent_object='me', connection_name='feed', message='Roar Lions!')
