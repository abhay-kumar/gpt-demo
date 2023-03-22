# Import necessary packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
from llama_index import download_loader
import os

os.environ['OPENAI_API_KEY'] = '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'

'''
# Loading from a directory
documents = SimpleDirectoryReader('store').load_data()

# Loading from web
BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")
loader = BeautifulSoupWebReader()
web_documents = loader.load_data(urls=[
    'https://razorpay.com/docs/'
    'https://razorpay.com/pricing/',
    'https://razorpay.com/docs/api',
    'https://razorpay.com/support/',
    'https://razorpay.com/docs/get-started',
    'https://razorpay.com/docs/payments',
    'https://razorpay.com/docs/x',
    'https://razorpay.com/docs/partners',
    'https://razorpay.com/docs/payments/customers/customer-refunds',
    'https://razorpay.com/docs/#home-payments',
    'https://razorpay.com/docs/#home-banking',
    'https://razorpay.com/docs/#home-partners',
    'https://razorpay.com/docs/#home-devtools',
    'https://razorpay.com/docs/payments/payment-gateway/web-integration/standard/',
    'https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/',
    'https://razorpay.com/docs/payments/payment-gateway/ios-integration/standard/',
    'https://razorpay.com/docs/payments/payment-gateway/ecommerce-plugins/',
    'https://razorpay.com/docs/payments/payment-gateway/android-integration/standard/',
    'https://razorpay.com/docs/payments/payment-gateway/get-started/',
    'https://razorpay.com/docs/x/get-started/sign-up/',
    'https://razorpay.com/docs/x/payouts/',
    'https://razorpay.com/docs/x/bulk-payouts/',
    'https://razorpay.com/docs/x/get-started/test-mode/',
    'https://razorpay.com/docs/partners/resellers/',
    'https://razorpay.com/docs/partners/aggregators/',
    'https://razorpay.com/docs/partners/platform/',
    'https://razorpay.com/docs/partners/commissions/',
    'https://razorpay.com/docs/api/',
    'https://razorpay.com/docs/webhooks/',
    'https://razorpay.com/docs/payments/server-integration/',
    'https://razorpay.com/docs/api/errors/',
    'https://razorpay.com/integrations',
    'https://razorpay.com/x',
    'https://razorpay.com/x/current-accounts',
    'https://razorpay.com/x/payouts',
    'https://razorpay.com/x/payout-links',
    'https://razorpay.com/x/corporate-cards',
    'https://razorpay.com/capital',
    'https://razorpay.com/capital/instant-settlements',
    'https://razorpay.com/capital/working-capital-loans',
    'https://razorpay.com/x/instant-settlements-for-marketplace/',
    'https://razorpay.com/partners',
    'https://razorpay.com/partners/onboarding-apis/',
    'https://razorpay.com/route/',
    'https://razorpay.com/invoices/',
    'https://razorpay.com/freelancer-unregistered-business/',
    'https://razorpay.com/accept-international-payments/',
    'https://razorpay.com/flashcheckout/',
    'https://razorpay.com/upi/',
    'https://razorpay.com/bharatqr/',
    'https://razorpay.com/epos/',
    'https://razorpay.com/demo/',
    'https://razorpay.com/payroll/',
    'https://razorpay.com/payment-gateway',
    'https://razorpay.com/magic',
    'https://razorpay.com/payment-pages',
    'https://razorpay.com/payment-links',
    'https://razorpay.com/qr-code',
    'https://razorpay.com/subscriptions',
    'https://razorpay.com/smart-collect',
    'https://razorpay.com/docs',
    'https://razorpay.com/docs/api',
    'https://razorpay.com/blog',
    'https://razorpay.com/customer-stories',
    'https://razorpay.com/events',
    'https://razorpay.com/chargeback',
    'https://razorpay.com/settlement',
    'https://razorpay.com/solutions/education',
    'https://razorpay.com/solutions/e-commerce/',
    'https://razorpay.com/solutions/saas/',
    'https://razorpay.com/solutions/bfsi/',
    'https://razorpay.com/gst-calculator',
    'https://razorpay.com/x/tds-online-payment/',
    'https://razorpay.com/about',
    'https://razorpay.com/jobs',
    'https://razorpay.com/terms',
    'https://razorpay.com/privacy',
    'https://razorpay.com/responsible-disclosure',
    'https://razorpay.com/support',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/addon.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/card.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/customers.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/emandate.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/fund.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/invoice.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/item.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/order.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/papernach.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/payment.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/paymentLink.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/paymentVerfication.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/plan.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/qrcode.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/refund.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/registerEmandate.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/registerNach.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/settlement.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/subscription.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/token.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/transfer.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/upi.md',
    'https://github.com/razorpay/razorpay-java/blob/master/documents/virtualAccount.md',
    'https://medium.com/@laraveltuts/laravel-9-integrate-razorpay-payment-gateway-491569c13a99',
    'https://www.learndash.com/support/docs/core/settings/razorpay-integration/',
    'https://enappd.com/blog/how-to-integrate-razorpay-in-ionic-4-apps-and-pwa/20/',
    'https://www.javatpoint.com/razorpay-integration-in-ios',
    'https://javascript.plainenglish.io/razorpay-integration-with-node-js-4915d03ad8ce'
])

# Construct a simple vector index
index = GPTSimpleVectorIndex(documents + web_documents)

# Save your index to a index.json file
index.save_to_disk('index.json')
'''

# Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Querying the index
response = index.query("What is smart collect?")
print(response)
