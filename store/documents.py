from django_elasticsearch_dsl import DocType, Index, fields
from elasticsearch_dsl import analyzer
from .models import Product, Store

products = Index('product')

html_strip = analyzer(
  'html_strip',
  tokenizer="standard",
  filter=["standard", "lowercase", "stop", "snowball"],
  char_filter=["html_strip"]
)

@products.doc_type
class ProductDocument(DocType):

  id = fields.IntegerField(attr='id')

  title = fields.StringField(
    analyzer=html_strip,
    fields={
      'raw': fields.StringField(analyzer='keyword'),
    }
  )

  store = fields.IntegerField(
    attr='store_indexing',
    # analyzer=html_strip,
  )

  # store = NestedField(properties={
  #   'id': IntegerField(),
  #   'title': StringField(),
  # })

  class Meta:
    model = Product

    related_models = [Store]
  
  def get_instances_from_related(self, related_instance):
    if isinstance(related_instance, Store):
      return related_instance.product_set.all()