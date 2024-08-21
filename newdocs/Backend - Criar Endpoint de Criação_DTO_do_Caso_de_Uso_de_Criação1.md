```csharp
namespace Project.Application.UseCases.Brands.CreateBrand
{
    public record CreateBrandDto(
        string Id, 
        Organization Organization, 
        Category Category, 
        string Name, 
        string? Title);
}
```