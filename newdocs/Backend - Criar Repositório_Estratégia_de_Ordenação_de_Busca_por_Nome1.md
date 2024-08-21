```csharp
namespace Project.Domain.Brands.OrderStrategies
{
    public class OrderByNameStrategy : StringOrder<Brand>
    {
        public OrderByNameStrategy(bool descending = false) 
        { 
            Descending = descending; 
        }

        public override Expression<Func<Brand, string>> ToExpression()
        {
            return brand => brand.Name;
        }
    }
}
```