from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class User_throttle(UserRateThrottle):
    scope = 'user_requests_limit'