```csharp
namespace Project.Application.UseCases.Brands.GetAllBrands
{
    public class GetAllBrandsQuery : IQuery<PaginatedResponse<GetAllBrandsDto>>
    {
        public string? BrandIdOrName { get; }
        public IEnumerable<string>? BrandIds { get; }
        public BrandOrderBy OrderBy { get; }
        public bool? OrderByDescending { get; }
        public int? Offset { get; }
        public int? Limit { get; }

        public GetAllBrandsQuery(string? brandIdOrName, IEnumerable<string>? brandIds, BrandOrderBy orderBy, bool? orderByDescending, int? offset, int? limit)
        {
            BrandIdOrName = brandIdOrName;
            BrandIds = brandIds;
            OrderBy = orderBy;
            OrderByDescending = orderByDescending;
            Offset = offset;
            Limit = limit;
        }
    }

    public enum BrandOrderBy
    {
        Id,
        Name,
        CreateDate
    }
}
```