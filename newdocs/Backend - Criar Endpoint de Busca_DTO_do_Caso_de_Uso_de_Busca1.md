```csharp
namespace Project.Application.UseCases.Brands.GetAllBrands
{
    public record GetAllBrandsDto(
        string Id, 
        string Name, 
        string? Title);
}
```