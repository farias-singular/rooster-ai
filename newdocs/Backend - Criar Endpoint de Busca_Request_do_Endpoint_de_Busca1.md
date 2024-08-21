```csharp
namespace Project.API.Controllers.Organizations.APIs.Brands.Endpoints.GetAllBrands
{
    public class GetAllBrandsRequest
    {
        public string? BrandIdOrName { get; set; }
        public IEnumerable<string>? BrandIds { get; set; }
        public BrandOrderBy OrderBy { get; set; } = BrandOrderBy.Name;
        public bool? OrderByDescending { get; set; } = false;
        public int? Offset { get; set; } = 0;
        public int? Limit { get; set; } = 10;
    }
}
```