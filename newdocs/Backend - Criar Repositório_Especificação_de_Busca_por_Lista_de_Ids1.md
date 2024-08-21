```csharp
namespace Project.Domain.Brands.Specifications
{
    public class BrandIdIsContainedInSpecification : Specification<Brand>
    {
        private readonly IEnumerable<string> _ids;

        public BrandIdIsContainedInSpecification(IEnumerable<string> ids)
        {
            _ids = ids;
        }

        public override Expression<Func<Brand, bool>> ToExpression()
        {
            return brand => _ids.Contains(brand.Id);
        }
    }
}
```