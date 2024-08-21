```csharp
namespace Project.Domain.Brands.Specifications
{
    public class BrandIdOrNameSpecification : Specification<Brand>
    {
        private readonly string _idOrName;
        
        public BrandIdOrNameSpecification(string idOrName)
        {
            _idOrName = idOrName;
        }
    
        public override Expression<Func<Brand, bool>> ToExpression()
        {
            return brand =>
                brand.Id.ToLower().Contains(_idOrName.ToLower()) ||
                brand.Name.ToLower().Contains(_idOrName.ToLower());
        }
    }
}
```