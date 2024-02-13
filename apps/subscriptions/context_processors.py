# from django.conf import settings
# from django.contrib.auth.models import AnonymousUser
# import stripe
# from .models import StripeCustomer

# def subscription_status(request):
#     if not request.user.is_authenticated:
#         # Return an empty context if the user is not authenticated
#         return {'subscription': None}

#     try:
#         # Retrieve the StripeCustomer object associated with the current user
#         stripe_customer = StripeCustomer.objects.get(user=request.user)
#         # Set the Stripe API key
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         # Retrieve the subscription using the Stripe API
#         subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
#         # Return the subscription in the context
#         return {'subscription': subscription}
#     except StripeCustomer.DoesNotExist:
#         # Handle the case where the StripeCustomer does not exist for the user
#         return {'subscription': None}
#     except stripe.error.StripeError as e:
#         # Handle potential Stripe API errors (e.g., network issues, invalid IDs)
#         # Log the error or send it to monitoring software if necessary
#         # For simplicity, we're returning None here, but you might want to handle this differently
#         return {'subscription': None}




from django.conf import settings
from django.contrib.auth.models import AnonymousUser
import stripe
from .models import StripeCustomer  # Assuming you have a Product model

def subscription_status(request):
    if not request.user.is_authenticated:
        # Return an empty context if the user is not authenticated
        return {'subscription': None, 'product': None}

    try:
        # Retrieve the StripeCustomer object associated with the current user
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        # Set the Stripe API key
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Retrieve the subscription using the Stripe API
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        # Assume you have a way to relate a product to a subscription or user, adjust as needed
        product = stripe.Product.retrieve(subscription.plan.product)
        # Return the subscription and product in the context
        return {'subscription': subscription, 'product': product}
    except (StripeCustomer.DoesNotExist):
        # Handle the case where the StripeCustomer or Product does not exist for the user
        return {'subscription': None, 'product': None}
    except stripe.error.StripeError as e:
        # Handle potential Stripe API errors
        # Log the error or send it to monitoring software if necessary
        return {'subscription': None, 'product': None}
