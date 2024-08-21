```csharp
namespace Project.Application.UseCases.Brands.GetBrandById
{
    public record GetBrandByIdDto(
        string Id, 
        Organization Organization, 
        Category Category, 
        string Name, 
        string? Title);
}
```