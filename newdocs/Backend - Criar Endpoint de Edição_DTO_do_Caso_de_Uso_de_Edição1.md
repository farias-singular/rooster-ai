```csharp
namespace Project.Application.UseCases.Brands.UpdateBrand
{
    public record UpdateBrandDto(
        string Id, 
        Organization Organization, 
        Category Category, 
        string Name, 
        string? Title);
}
```