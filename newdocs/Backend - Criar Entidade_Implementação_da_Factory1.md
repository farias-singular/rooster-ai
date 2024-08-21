```csharp
namespace Project.Domain.Brands
{
    public class BrandFactory : IBrandFactory
    {
        private readonly IBrandUniquenessChecker _brandUniquenessChecker;

        public BrandFactory(IBrandUniquenessChecker brandUniquenessChecker)
        {
            _brandUniquenessChecker = brandUniquenessChecker;
        }

        public Brand Create(
            string id,
            Organization organization,
            Category category,
            string name,
            string? title)
        {
            return Brand.Create(
                id, 
                organization, 
                category, 
                name, 
                title, 
                _brandUniquenessChecker);
        }
    }
}
```