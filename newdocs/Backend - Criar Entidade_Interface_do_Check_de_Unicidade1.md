```csharp
namespace Project.Domain.Brands
{
    public interface IBrandUniquenessChecker
    {
        bool IsUnique(string id, string organizationId);
        
        Task<bool> IsUniqueAsync(string id, string organizationId);
    }
}
```