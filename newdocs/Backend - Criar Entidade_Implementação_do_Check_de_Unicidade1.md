```csharp
namespace Project.Infrastructure.Domain.Brands
{
    public class BrandUniquenessChecker : IBrandUniquenessChecker
    {
        private readonly MultitenantContext _context;

        public BrandUniquenessChecker(MultitenantContext context)
        {
            _context = context;
        }

        public bool IsUnique(string id, string organizationId)
        {
            return !_context.Brands.Any(b => b.Id == id && b.OrganizationId == organizationId);
        }

        public async Task<bool> IsUniqueAsync(string id, string organizationId)
        {
            return !await _context.Brands.AnyAsync(b => b.Id == id && b.OrganizationId == organizationId);
        }
    }
}
```