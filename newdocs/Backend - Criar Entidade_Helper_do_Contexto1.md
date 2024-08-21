```csharp
namespace Project.Tests.Infrastructure
{
    public partial class MultitenantContextHelper
    {
        public async Task<IEnumerable<Brand>> AddBrandsAsync(List<Brand>? brands = null)
        {
            brands ??= EntityFaker.RandomBrands(10);
            
            await _context.Brands.AddRangeAsync(brands);

            await _context.SaveChangesAsync();

            return _context.Brands;
        }
    }
}
```