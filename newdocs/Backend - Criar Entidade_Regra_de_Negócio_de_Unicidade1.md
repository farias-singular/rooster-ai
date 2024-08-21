```csharp
namespace Project.Domain.Brands.Rules
{
    public class BrandIdMustBeValidRule : IBusinessRule
    {
        private readonly IBrandUniquenessChecker _brandUniquenessChecker;
        private readonly string _id;
        private readonly string _organizationId;

        public BrandIdMustBeValidRule(
            IBrandUniquenessChecker brandUniquenessChecker, 
            string id,
            string organizationId)
        {
            _brandUniquenessChecker = brandUniquenessChecker;
            _id = id;
            _organizationId = organizationId;
        }

        public bool IsBroken() => 
            !_brandUniquenessChecker.IsUnique(_id, _organizationId);

        public string Message => "Brand is not unique or is invalid.";
    }
}
```