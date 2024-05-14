from behave import *
import requests
import json
# from features.steps.utils import post_store_api_request,verify_post_api_response

response=""


@given(u'User posts a request')
def user_post_request(context):
    print("User Sends post api Request")



@when(u'request "{url}" is successfull')
def post_store_api(context,url):
    # post_store_api_request(url)
    data = [{"actor":{},"context":{"contextActivities":{"parent":[{"id":"https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a"}],"category":[{"id":"https://elucidat.com","definition":{"name":{"en-US":"Elucidat.com"},"description":{"en-US":"Course lovingly crafted with the Elucidat.com rapid authoring tool"}}}]},"registration":"09a8a2e8-0c93-11ef-95a6-0a328b41cb01"},"object":{"objectType":"Activity","definition":{"type":"http://activitystrea.ms/schema/1.0/page","name":{"en-US":"YOU DECIDE"}},"id":"https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a/5c9126fe4f952"},"verb":{"id":"http://adlnet.gov/expapi/verbs/experienced","display":{"en-US":"experienced"}},"result":{"extensions":{"https://app.elucidat.com/xapi/progress":20},"completion":"false"},"timestamp":"2024-05-10T14:12:28.187Z"}]
    headers = {'Authorization': 'Basic NTc0MTk3OTg5NGFkMDpXa1Y1VXpaaVdWTlhUa3A2VDNsdFRsbFpORlpzVkM5Rk5VdzBibkZLVDBGUFMyeFNMMnhKTlZKSlZFWnpVMUZzYW5OM1ZYWmtOVGd4WjBsdmRFUkNVbFY2TlhsT2F6QmhOakpvVkVGeFdXOVJWMUo2ZDFnM1NVeE1TMFl5ZUZOV04ybDVkbXhvY0ZGV1dHYzk='}
    # Send POST request with JSON data
    global response
    response = requests.post(url, json=data,headers=headers)
    print(response.json())


@then(u'User should be able to verify the response "{status}"')
def verify_store_api(context,status):
    # verify_post_api_response(status)
    json_res = response.json()
    assert json_res.get("status") == status, "rest end point store must return status -> "+ status +" but it returned -> %s" %json_res.get("status")

    