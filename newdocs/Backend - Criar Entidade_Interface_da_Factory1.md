```csharp
namespace Project.Domain.Brands
{
    public interface IBrandFactory
    {
        Brand Create(
            string id,
            Organization organization,
            Category category,
            string name,
            string? title);
    }
}
```